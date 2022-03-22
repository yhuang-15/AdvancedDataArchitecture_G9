import datetime
from flask import jsonify
from daos.waitingList_dao import WaitingListDAO
from db import Session


class Status:
    @staticmethod
    def update(w_id, status):
        session = Session()
        waitingList = session.query(WaitingListDAO).filter(WaitingListDAO.id == w_id)[0]
        waitingList.status.status = status
        waitingList.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The waitinglist status was updated'}), 200
    
    @staticmethod
    def post_status():
        return jsonify({'message': 'no method'}), 405

    @staticmethod
    def get_status():
        return jsonify({'message': 'no method'}), 405

    @staticmethod
    def delete_status():
        return jsonify({'message': 'no method'}), 405
