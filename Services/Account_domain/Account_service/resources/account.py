from datetime import datetime
from sqlalchemy import update
from flask import jsonify

from daos.account_dao import AccountDAO
from db import Session


class Account:
    @staticmethod
    def create(body):
        session = Session()
        account = AccountDAO( body['account_id'], body['first_name'], body['last_name'], 
                              body['phone_number'], body['email_address'],  
                               datetime.strptime(body['down_time'], '%Y-%m-%d %H:%M:%S.%f'),
                               body['premium_status'], body['preference'], body['in_waiting_list'], body['has_contract'], body['bank_account'])
        session.add(account)
        session.commit()
        session.refresh(account)
        session.close()
        return jsonify({'Account created! Acount ID': account.id}), 200

    @staticmethod
    def get(a_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        account = session.query(AccountDAO).filter(AccountDAO.id == int(a_id)).first()

        if account:
            text_out = {
                "account_id:": account.account_id,
                "first_name": account.first_name,
                "last_name": account.last_name,
                "phone_number": account.phone_number,
                "email_address": account.email_address,
                "down_time": account.down_time.isoformat(),
                "premium_status": account.premium_status,
                "preference": account.preference,
                "in_waiting_list": account.in_waiting_list,
                "has_contract": account.has_contract,
                "bank_account": account.bank_account
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no account with id {a_id}'}), 404
            
    @staticmethod
    def delete(a_id):
         session = Session()
         effected_rows = session.query(AccountDAO).filter(AccountDAO.id == int(a_id)).delete()
         session.commit()
         session.close()
         if effected_rows == 0:
             return jsonify({'message': f'There is no account with id {a_id}'}), 404
         else:
             return jsonify({'message': 'The account has been deleted'}), 200
     
    @staticmethod
    def update(a_id, body):
        session = Session()

        accounts = session.query(AccountDAO).filter(AccountDAO.id == a_id)
        account = accounts.all()

        if len(account) != 0:
            accounts.update(body)
            session.commit()
            session.close()
            return jsonify({'message': 'The account has been updated'}), 200
        else:
            session.close()
            return jsonify({'message': f'No account with id {a_id}'}), 404
        
    @staticmethod
    def error_405():
        return jsonify({'message': 'Method not allowed'}), 405

    @staticmethod
    def list_all_accounts():
        session = Session()
        all_accounts = session.query(AccountDAO).all()
        session.close()

        if len(all_accounts) == 0:
            return jsonify({'message': 'No account in DB'}), 200
        else:
            text_out = {
                "account_id:": all_accounts[0].account_id,
                "first_name": all_accounts[0].first_name,
                "last_name": all_accounts[0].last_name,
                "phone_number": all_accounts[0].phone_number,
                "email_address": all_accounts[0].email_address,
                "down_time": all_accounts[0].down_time.isoformat(),
                "premium_status": all_accounts[0].premium_status,
                "preference": all_accounts[0].preference,
                "in_waiting_list": all_accounts[0].in_waiting_list,
                "has_contract": all_accounts[0].has_contract,
                "bank_account": all_accounts[0].bank_account
            }
            if len(all_accounts) == 1:
                text_out["Next account id"] = 'only 1 account available'
            else:
                text_out["Next account id"] = all_accounts[0].id
            return jsonify(text_out), 200

    @staticmethod
    def delete_all():
        sql = 'delete from account'
        session = Session()
        session.execute(sql)
        session.commit()
        session.close()

        return jsonify({'message': 'deleted all accounts'}), 200

