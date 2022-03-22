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
            return jsonify({'message': f'There is no delivery with id {a_id}'}), 404
            
    @staticmethod
    def delete(a_id):
         session = Session()
         effected_rows = session.query(AccountDAO).filter(AccountDAO.id == int(a_id)).delete()
         session.commit()
         session.close()
         if effected_rows == 0:
             return jsonify({'message': f'There is no delivery with id {a_id}'}), 404
         else:
             return jsonify({'message': 'The delivery was removed'}), 200
     
    @staticmethod
    def update(a_id, body):
        session = Session()

        session.query(AccountDAO).filter(AccountDAO.id == a_id).update(body)

        session.commit()
        return jsonify({'message': 'The account has been updated'}), 200
