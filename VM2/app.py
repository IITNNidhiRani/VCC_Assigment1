from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Dummy order data
orders = {
    101: {"user_id": 1, "product": "Tablet", "amount": 1500},
    102: {"user_id": 2, "product": "Phone", "amount": 600}
}

USER_SERVICE_URL = "http://192.168.196.189:6000/users/"  

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id, None)
    if not order:
        return jsonify({"error": "Order not found"}), 404

     # Fetch user details from User Service
     user_response = requests.get(f"{USER_SERVICE_URL}{order['user_id']}") 
     if user_response.status_code == 200: 
        order["user_details"] = user_response.json() 
     else: 
        order["user_details"] = "User details unavailable" 
        
     return jsonify(order) 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
