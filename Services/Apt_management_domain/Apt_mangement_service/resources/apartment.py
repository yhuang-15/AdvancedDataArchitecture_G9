from datetime import datetime
from dbm import dumb
from ftplib import all_errors
from pydoc import apropos
from re import A
import json

from flask import jsonify, session

from constant import STATUS_AVAILABLE, STATUS_OCCUPIED
from daos.apartment_dao import ApartmentDAO
from daos.status_dao import StatusDAO
from db import Session

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime):
        return obj.isoformat()


class Apartment:
    @staticmethod
    def create(body):
        session = Session()
        apartment = ApartmentDAO(body['size'], body['price'])
                            #    , datetime.strptime(body['start_date'], '%Y-%m-%d'), datetime.strptime(body['end_date'], '%Y-%m-%d')
        session.add(apartment)
        session.commit()
        session.refresh(apartment)
        session.close()
        return jsonify({'apartment_id': apartment.id}), 200

    @staticmethod
    def get(apt_id):
        session = Session()
        apartment = session.query(ApartmentDAO).filter(ApartmentDAO.id == apt_id).first()

        if apartment != None:
            status_obj = apartment.status
            text_out = {
                "size:": apartment.size,
                "price": apartment.price,
                "status": {
                    "status": status_obj.status,
                    "start_date": status_obj.start_date,
                    "end_date": status_obj.end_date,
                    "last_update": status_obj.last_update.isoformat()
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no apartment with id {apt_id}'}), 404

    @staticmethod
    def delete(apt_id):
        session = Session()
        affected_rows = session.query(ApartmentDAO).filter(ApartmentDAO.id == apt_id).delete()
        session.commit()
        session.close()
        if affected_rows == 0:
            return jsonify({'message': f'There is no apartment with id {apt_id}'}), 404
        else:
            return jsonify({'message': 'The apartment was removed'}), 200

    @staticmethod
    def list():
        session = Session()
        all_apartments = session.query(ApartmentDAO).all()
        end_list = []
        for apt in all_apartments:
            status_obj = apt.status
            text_out = {
                "size:": apt.size,
                "price": apt.price,
                "status": {
                    "status": status_obj.status,
                    "start_date": status_obj.start_date,
                    "end_date": status_obj.end_date,
                    "last_update": status_obj.last_update.isoformat()
                }
            }
            end_list.append(text_out)

        session.close()
        return json.dumps(end_list, default=alchemyencoder)

    @staticmethod
    def update_apt(apt_id, body):
        session = Session()
        apartment = session.query(ApartmentDAO).filter(ApartmentDAO.id == apt_id)

        if apartment != None:
            apartment.update({ "size": body['size'], "price": body['price']})

        else:
            return jsonify({'message': f'There is no apartment with id {apt_id}'}), 404

        session.commit()
        session.refresh(apartment.first())
        session.close()
        return jsonify({'apartment_id': apartment.first().id}), 200


    @staticmethod
    def delete_all():
        sql = 'delete from apartment'
        session = Session()
        session.execute(sql)
        session.commit()
        session.close()

        return jsonify({'message': 'deleted all apartments'}), 200

    @staticmethod
    def bulk_update():
        return jsonify({'message': 'Bulk updating, not available. Update apartments one by one.'}), 405
    
    @staticmethod
    def post_id():
        return jsonify({'message': 'no method'}), 405


    
