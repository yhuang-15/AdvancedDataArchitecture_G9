from datetime import datetime

from flask import jsonify

from daos.application_dao import ApplicationDAO
from daos.status_dao import StatusDAO
from db import Session
import json

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime):
        return obj.isoformat()

class Application:
    @staticmethod
    def create(body):
        session = Session()
        application = ApplicationDAO(body['application_id'], body['user_id'], body['apartment_id'], datetime.now(),
                               StatusDAO("STATUS_CREATED", datetime.now()))
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
                "application_id": application.application_id,
                "user_id:": application.user_id,
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

    @staticmethod
    def list():
        session = Session()
        all_applications = session.query(ApplicationDAO).all()
        end_list = []
        for application in all_applications:
            status_obj = application.status
            text_out = {
                "application_id": application.application_id,
                "user_id:": application.user_id,
                "apartment_id": application.apartment_id,
                "application_time": application.application_time.isoformat(),
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            end_list.append(text_out)

        session.close()
        return json.dumps(end_list, default=alchemyencoder)

    @staticmethod
    def update_application(a_id, body):
        session = Session()
        application = session.query(ApplicationDAO).filter(ApplicationDAO.application_id == a_id)

        if application:
            application.update({"user_id": body['user_id'],
                                "apartment_id": body['apartment_id']})

        else:
            return jsonify({'message': f'There is no application with id {a_id}'}), 404

        session.commit()
        session.refresh(application.first())
        session.close()
        return jsonify({'application_id': application.first().application_id}), 200

    @staticmethod
    def delete_all():
        sql = 'delete from application'
        session = Session()
        session.execute(sql)
        session.commit()
        session.close()

        return jsonify({'message': 'deleted all applications'}), 200

    @staticmethod
    def bulk_update():
        return jsonify({'message': 'Bulk updating, not available. Update applications one by one.'}), 405

    @staticmethod
    def post_id():
        return jsonify({'message': 'no method'}), 405