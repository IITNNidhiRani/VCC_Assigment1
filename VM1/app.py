from flask import Flask, jsonify

app = Flask(__name__)

# Dummy user data
users = {
    1: {"name": "Alisha", "email": "alisha@example.com"},
    2: {"name": "Putus", "email": "putus@example.com"}
}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id, None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
