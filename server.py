from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["coffee_app"]
orders_collection = db["orders"]

@app.route('/confirm-order', methods=['POST'])
def confirm_order():
    try:
        data = request.json  # Get JSON data from request

        if not data:
            return jsonify({"error": "No data received"}), 400

        # Insert order into MongoDB
        order_id = orders_collection.insert_one(data).inserted_id

        return jsonify({"message": "Order placed successfully", "order_id": str(order_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host="192.168.242.1")
