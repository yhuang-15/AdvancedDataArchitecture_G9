from flask import Flask, request

from db import Base, engine
from resources.account import Account


app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/accounts', methods=['POST'])
def create_account():
    req_data = request.get_json()
    return Account.create(req_data)


#@app.route('/deliveries/<d_id>', methods=['GET'])
#def get_account(d_id):
#    return Delivery.get(d_id)


@app.route('/accounts/<a_id>', methods=['PUT'])
def update_account(a_id):
    req_data = request.get_json()
    return Account.update(a_id, req_data)


#@app.route('/deliveries/<d_id>', methods=['DELETE'])
#def delete_account(d_id):
#    return Delivery.delete(d_id)
#

app.run(host='0.0.0.0', port=5000)
