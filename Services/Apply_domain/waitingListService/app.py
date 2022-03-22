from flask import Flask, request

from db import Base, engine
from resources.waitingList import WaitingList
from resources.status import Status

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/waitingList', methods=['POST'])
def create_waiting_list_entry():
    req_data = request.get_json()
    return WaitingList.create(req_data)


@app.route('/waitingList', methods=['GET'])
def list_waiting_list():
    req_data = request.get_json()
    return WaitingList.list()

@app.route('/waitingList', methods=['PUT'])
def bulk_update():
    req_data = request.get_json()
    return WaitingList.bulk_update()

@app.route('/waitingList', methods=['DELETE'])
def drop_waiting_list():
    req_data = request.get_json()
    return WaitingList.delete_all()


@app.route('/apartments/<w_id>', methods=['POST'])
def create_waiting_list_id(w_id):
    return WaitingList.post_id()


@app.route('/waitingList/<w_id>', methods=['GET'])
def get_waiting_list_id(w_id):
    return WaitingList.get(w_id)


@app.route('/waitingList/<w_id>', methods=['PUT'])
def update_waiting_list_id(w_id):
    req_data = request.get_json()
    return WaitingList.update_wl(w_id, req_data)


@app.route('/waitingList/<w_id>', methods=['DELETE'])
def delete_waiting_list_id(w_id):
    return WaitingList.delete(w_id)


@app.route('/apartments/<w_id>/status', methods=['POST'])
def create_waiting_list_entry_status(w_id):
    return Status.post_status()

@app.route('/apartments/<w_id>/status', methods=['GET'])
def get_waiting_list_status(w_id):
    return Status.get_status()

@app.route('/waitingList/<w_id>/status', methods=['PUT'])
def update_waiting_list_entry(w_id):
    status = request.args.get('status')
    return Status.update(w_id, status)

@app.route('/waitingList/<w_id>/status', methods=['DELETE'])
def delete_waiting_list_status(w_id):
    return Status.delete_status()













app.run(host='0.0.0.0', port=5000)
