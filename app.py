from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask import render_template
import requests
import os

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/shipping_db')
mongo = PyMongo(app)

@app.route('/new_parcel', methods=['POST'])
def receive_parcel():
    data = request.json
    try:
        order_id = data['order_id']
        user_id = data['user_id']
        parcel_id = data['parcel_id']
    except KeyError:
        return jsonify({'error': 'Missing data'}), 400

    user_address = get_user_address(user_id)
    if not user_address:
        return jsonify({'error': 'User address not found'}), 404

    status = 'Processing'
    mongo.db.parcels.insert_one({'parcel_id': parcel_id, 'order_id': order_id, 'user_id': user_id, 'address': user_address, 'status': status})
    send_to_dispatching(parcel_id, user_address)

    return jsonify({'message': 'Parcel information received successfully'})

@app.route('/all_parcels')
def web_interface():
    try:
        parcel_data = mongo.db.parcels.find()
    except Exception as e:
        return str(e), 500
    return render_template('index.html', parcel_data=parcel_data)

def send_to_dispatching(parcel_id, address):
    # =============================
    # call DISPATCHING microservice
    # POST parcel_id and address
    # =============================
    pass

def get_user_address(user_id):
    # =============================
    # call USERS microservice
    # GET address from user_id
    # =============================
    return 'Unknown'

if __name__ == '__main__':
    app.run(debug=False)
