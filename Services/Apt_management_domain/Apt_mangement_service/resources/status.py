import datetime
from flask import jsonify
from daos.apartment_dao import ApartmentDAO
from daos.status_dao import StatusDAO
from db import Session
from constant import STATUS_AVAILABLE, STATUS_OCCUPIED



class Status:
    @staticmethod
    def update_status(apt_id, body):
        session = Session()
        apartment = session.query(ApartmentDAO).filter(ApartmentDAO.id == apt_id).first()

        if apartment:

            apartment.status.last_update = datetime.datetime.now()

            if body['status'] == 'available':
                apartment.status.status = STATUS_AVAILABLE 

            elif body['status'] == 'occupied':
                apartment.status.status =  STATUS_OCCUPIED
                apartment.status.start_date =str(body['start_date'])
                apartment.status.end_date =str(body['end_date'])
        else:
            return jsonify({'message': f'no apartment with id: {apt_id}'}), 404
  
        session.commit()
        session.close()
        return jsonify({'message': 'The apartment status was updated'}), 200

    @staticmethod
    def post_status():
        return jsonify({'message': 'no method'}), 405

    @staticmethod
    def get_status(apt_id):
         session = Session()
         apartment = session.query(ApartmentDAO).filter(ApartmentDAO.id == apt_id).first()
    
         if apartment:
             status_obj = apartment.status
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
             return jsonify({'message': f'There is no apartment with id {apt_id}'}), 404

    @staticmethod
    def delete_status():
        return jsonify({'message': 'no method'}), 405