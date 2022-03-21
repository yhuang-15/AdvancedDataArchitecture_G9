from flask import Flask, request

from db import Base, engine
from resources.waitingList import WaitingList
from resources.status import Status

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/waitingList', methods=['POST'])
def create_application():
    req_data = request.get_json()
    return WaitingList.create(req_data)


@app.route('/waitingList', methods=['GET'])
def list_waitingList():
    req_data = request.get_json()
    return WaitingList.list()


@app.route('/waitingList/<w_id>', methods=['GET'])
def get_waitingList(w_id):
    return WaitingList.get(w_id)


@app.route('/waitingList/<w_id>/status', methods=['PUT'])
def update_waitingList(w_id):
    status = request.args.get('status')
    return Status.update(w_id, status)


@app.route('/waitingList/<w_id>', methods=['DELETE'])
def delete_waitList(w_id):
    return WaitingList.delete(w_id)


app.run(host='0.0.0.0', port=5000)
