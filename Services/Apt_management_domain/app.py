from flask import Flask, request

from db import Base, engine
from resources.apartment import Apartment
from resources.status import Status

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/apartments', methods=['POST'])
def create_apartment():
    req_data = request.get_json()
    return Apartment.create(req_data)

@app.route('/apartments', methods=['GET'])
def list_apartments():
    req_data = request.get_json()
    return Apartment.list()

@app.route('/apartments', methods=['PUT'])
def bulk_update():
    req_data = request.get_json()
    return Apartment.bulk_update()

@app.route('/apartments', methods=['DELETE'])
def drop_apartments():
    req_data = request.get_json()
    return Apartment.delete_all()



@app.route('/apartments/<apt_id>', methods=['POST'])
def create_apartment_id(apt_id):
    return Apartment.post_id()

@app.route('/apartments/<apt_id>', methods=['GET'])
def get_apartment(apt_id):
    return Apartment.get(apt_id)

@app.route('/apartments/<apt_id>', methods=['PUT'])
def update_apartment(apt_id):
    req_data = request.get_json()
    return Apartment.update_apt(apt_id, req_data)

@app.route('/apartments/<apt_id>', methods=['DELETE'])
def delete_apartment(apt_id):
    return Apartment.delete(apt_id)


@app.route('/apartments/<apt_id>/status', methods=['POST'])
def create_apartment_status(apt_id):
    return Status.post_status()

@app.route('/apartments/<apt_id>/status', methods=['GET'])
def get_apartment_status(apt_id):
    return Status.get_status()

@app.route('/apartments/<apt_id>/status', methods=['PUT'])
def update_apartment_status(apt_id):
    req_data = request.get_json()
    return Status.update_status(apt_id, req_data)

@app.route('/apartments/<apt_id>/status', methods=['DELETE'])
def delete_apartment_status(apt_id):
    return Status.delete_status()




app.run(host='0.0.0.0', port=5000)
