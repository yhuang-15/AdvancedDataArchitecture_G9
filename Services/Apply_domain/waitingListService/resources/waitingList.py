from datetime import datetime, timedelta

from flask import jsonify

from constant import STATUS_WAITING
from daos.waitingList_dao import WaitingListDAO
from daos.status_dao import StatusDAO
from db import Session
import json

class WaitingList:
    @staticmethod
    def create(body):
        session = Session()
        waitingList = WaitingListDAO(body['application_id'], datetime.strptime(body['registration_date'], '%Y-%m-%d'), 
                                     (datetime.now() - datetime.strptime(body['waiting_time'], '%Y-%m-%d')), body['priority_status'],
                                     StatusDAO(STATUS_WAITING, datetime.now()))
        session.add(waitingList)
        session.commit()
        session.refresh(waitingList)
        session.close()
        return jsonify({'waitingList_id': waitingList.id}), 200
    

    @staticmethod
    def get(w_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        waitingList = session.query(WaitingListDAO).filter(WaitingListDAO.id == w_id).first()

        if waitingList != 0:
            if waitingList.priority_status == 'emergency':
                status_obj = waitingList.status
                text_out = {
                    "application_id": waitingList.application_id,
                    "registration_date": waitingList.registration_date.isoformat(),
                    "waiting_time": str(waitingList.waiting_time + timedelta(days=+3650)),
                    "priority_status:": waitingList.priority_status,
                    "status": {
                        "status": status_obj.status,
                        "last_update": status_obj.last_update.isoformat(),
                    }
                }
            elif waitingList.priority_status == 'international':
                status_obj = waitingList.status
                text_out = {
                    "application_id": waitingList.application_id,
                    "registration_date": waitingList.registration_date.isoformat(),
                    "waiting_time": str(waitingList.waiting_time + timedelta(days=+365)),
                    "priority_status:": waitingList.priority_status,
                    "status": {
                        "status": status_obj.status,
                        "last_update": status_obj.last_update.isoformat(),
                    }
                }
            else:
                status_obj = waitingList.status
                text_out = {
                    "application_id": waitingList.application_id,
                    "registration_date": waitingList.registration_date.isoformat(),
                    "waiting_time": str(waitingList.waiting_time),
                    "priority_status:": waitingList.priority_status,
                    "status": {
                        "status": status_obj.status,
                        "last_update": status_obj.last_update.isoformat(),
                    }
                }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no applicant with id {w_id}'}), 404

    @staticmethod
    def delete(w_id):
        session = Session()
        effected_rows = session.query(WaitingListDAO).filter(WaitingListDAO.id == w_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no applicant with id {w_id}'}), 404
        else:
            return jsonify({'message': 'The applicant was removed'}), 200

    @staticmethod
    def list():
        session = Session()
        all_waitingList = session.query(WaitingListDAO).all()
        end_list = []
        for waitingList in all_waitingList:
            if waitingList.priority_status == 'emergency':
                status_obj = waitingList.status
                text_out = {
                    "application_id": waitingList.application_id,
                    "registration_date": waitingList.registration_date.isoformat(),
                    "waiting_time": str(waitingList.waiting_time + timedelta(days=+3650)),
                    "priority_status:": waitingList.priority_status,
                    "status": {
                        "status": status_obj.status,
                        "last_update": status_obj.last_update.isoformat(),
                    }
                }
            elif waitingList.priority_status == 'international':
                status_obj = waitingList.status
                text_out = {
                    "application_id": waitingList.application_id,
                    "registration_date": waitingList.registration_date.isoformat(),
                    "waiting_time": str(waitingList.waiting_time + timedelta(days=+365)),
                    "priority_status:": waitingList.priority_status,
                    "status": {
                        "status": status_obj.status,
                        "last_update": status_obj.last_update.isoformat(),
                    }
                }
            else:
                status_obj = waitingList.status
                text_out = {
                    "application_id": waitingList.application_id,
                    "registration_date": waitingList.registration_date.isoformat(),
                    "waiting_time": str(waitingList.waiting_time),
                    "priority_status:": waitingList.priority_status,
                    "status": {
                        "status": status_obj.status,
                        "last_update": status_obj.last_update.isoformat(),
                    }
                } 
            end_list.append(text_out)
        end_list = sorted(end_list, key=lambda d: int(d['waiting_time'][:4]), reverse=True) 

        session.close()
        return json.dumps(end_list)

