from flask import Flask, jsonify, request
import requests
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client.order_database
orders_collection = db.orders

@app.route('/orders', methods=['POST'])
def create_order():
    order = request.json
    user_id = order.get('user_id')
    
    # Check if user exists
    user_response = requests.get(f'http://user_service:5000/users/{user_id}')
    if user_response.status_code == 404:
        return jsonify({"error": "User not found"}), 404
    
    result = orders_collection.insert_one(order)
    order['_id'] = str(result.inserted_id)
    return jsonify(order), 201

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders_collection.find_one({'_id': ObjectId(order_id)})
    if order:
        order['_id'] = str(order['_id'])
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)