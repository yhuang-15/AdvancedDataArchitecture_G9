from datetime import datetime

from flask import jsonify

from constant import STATUS_CREATED
from daos.application_dao import ApplicationDAO
from daos.status_dao import StatusDAO
from db import Session


class Application:
    @staticmethod
    def create(body):
        session = Session()
        application = ApplicationDAO(body['user_id'], body['application_id'], body['apartment_id'], datetime.now(),
                               StatusDAO(STATUS_CREATED, datetime.now()))
        session.add(application)
        session.commit()
        session.refresh(application)
        session.close()
        return jsonify({'application_id': application.application_id}), 200

    @staticmethod
    def get(a_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        application = session.query(ApplicationDAO).filter(ApplicationDAO.application_id == a_id).first()

        if application:
            status_obj = application.status
            text_out = {
                "user_id:": application.user_id,
                "application_id": application.application_id,
                "apartment_id": application.apartment_id,
                "application_time": application.application_time.isoformat(),
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no application with id {a_id}'}), 404

    @staticmethod
    def delete(a_id):
        session = Session()
        effected_rows = session.query(ApplicationDAO).filter(ApplicationDAO.application_id == a_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no application with id {a_id}'}), 404
        else:
            return jsonify({'message': 'The application was removed'}), 200
