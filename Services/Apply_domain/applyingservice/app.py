from flask import Flask, request

from db import Base, engine
from resources.application import Application
from resources.status import Status

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/applications', methods=['POST'])
def create_application():
    req_data = request.get_json()
    return Application.create(req_data)


@app.route('/applications/<a_id>', methods=['GET'])
def get_application(a_id):
    return Application.get(a_id)


@app.route('/applications/<a_id>/status', methods=['PUT'])
def update_application_status(a_id):
    status = request.args.get('status')
    return Status.update(a_id, status)


@app.route('/applications/<a_id>', methods=['DELETE'])
def delete_application(a_id):
    return Application.delete(a_id)


app.run(host='0.0.0.0', port=5000)
