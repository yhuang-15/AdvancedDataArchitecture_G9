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

    #@staticmethod
    #def get(d_id):
    #    session = Session()
    #    # https://docs.sqlalchemy.org/en/14/orm/query.html
    #    # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
    #    delivery = session.query(DeliveryDAO).filter(DeliveryDAO.id == int(d_id)).first()
#
    #    if delivery:
    #        status_obj = delivery.status
    #        text_out = {
    #            "customer_id:": delivery.customer_id,
    #            "provider_id": delivery.provider_id,
    #            "package_id": delivery.package_id,
    #            "order_time": delivery.order_time.isoformat(),
    #            "delivery_time": delivery.delivery_time.isoformat()
    #        }
    #        session.close()
    #        return jsonify(text_out), 200
    #    else:
    #        session.close()
    #        return jsonify({'message': f'There is no delivery with id {d_id}'}), 404
#
    #@staticmethod
    #def delete(d_id):
    #    session = Session()
    #    effected_rows = session.query(DeliveryDAO).filter(DeliveryDAO.id == int(d_id)).delete()
    #    session.commit()
    #    session.close()
    #    if effected_rows == 0:
    #        return jsonify({'message': f'There is no delivery with id {d_id}'}), 404
    #    else:
    #        return jsonify({'message': 'The delivery was removed'}), 200
    #
    @staticmethod
    def update(a_id, body):
        session = Session()

        session.query(AccountDAO).filter(AccountDAO.id == a_id).\
                    update(body)

        session.commit()
        return jsonify({'message': 'The account has been updated'}), 200
