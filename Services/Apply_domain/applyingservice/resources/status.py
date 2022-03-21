import datetime
from flask import jsonify
from daos.application_dao import ApplicationDAO
from db import Session


class Status:
    @staticmethod
    def update(a_id, status):
        session = Session()
        application = session.query(ApplicationDAO).filter(ApplicationDAO.application_id == a_id).first()
        if application:
            application = session.query(ApplicationDAO).filter(ApplicationDAO.application_id == a_id)[0]
            application.status.status = status
            application.status.last_update = datetime.datetime.now()
            session.commit()
            return jsonify({'message': 'The application status was updated'}), 200
        else:
            session.close()
            return jsonify({'message': f'There is no application with id {a_id}'}), 404


        #return jsonify({'message': 'The application status was updated'}), 200

    @staticmethod
    def get_status(a_id):
        session = Session()
        application = session.query(ApplicationDAO).filter(ApplicationDAO.application_id == a_id).first()

        if application:
            status_obj = application.status
            text_out = {
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
