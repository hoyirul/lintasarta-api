from flask import Flask, request, jsonify

app = Flask(__name__)

# Anggap saja ini adalah api seller yang sudah dibuat dan akan dilisting di marketplace.
tokens = {
    "sellerA": "TOKEN-SELLER-A",
    "sellerB": "TOKEN-SELLER-B"
  }

# Seller API A
@app.route('/api/a', methods=['GET', 'POST'])
def api_a():
    token = request.headers.get('Authorization')
    if token != f'Bearer {tokens["sellerA"]}':
        return jsonify({"error": "Invalid token"}), 401
    
    if request.method == 'POST':
        body = {
            "name": request.json.get("name"),
            "price": request.json.get("price")
        }

        if not body["name"] or not body["price"]:
            return jsonify({"error": "Invalid body"}), 400

        return jsonify({"message": "Welcome to API A, POST method"}), 201
    
    return jsonify({"message": "Welcome to API A"}), 200

# Seller API A PUT and DELETE
@app.route('/api/a/<id>', methods=['PUT', 'DELETE'])
def api_a_put_delete(id):
    token = request.headers.get('Authorization')
    if token != f'Bearer {tokens["sellerA"]}':
        return jsonify({"error": "Invalid token"}), 401

    if request.method == 'PUT':
        body = {
            "name": request.json.get("name"),
            "price": request.json.get("price")
        }

        if not body["name"] or not body["price"]:
            return jsonify({"error": "Invalid body"}), 400

        return jsonify({"message": "Welcome to API A, PUT method"}), 200

    if request.method == 'DELETE':
        return jsonify({"message": "Welcome to API A, DELETE method"}), 200

    return jsonify({"error": "Method not allowed"}), 405

# Seller API B
@app.route('/api/b', methods=['GET', 'POST'])
def api_b():
    token = request.headers.get('Authorization')
    if token != f'Bearer {tokens["sellerB"]}':
        return jsonify({"error": "Invalid token"}), 401
    
    if request.method == 'POST':
        return jsonify({"message": "Welcome to API B, POST method"}), 201

    return jsonify({"message": "Welcome to API B"}), 200

# Run the seller server
if __name__ == '__main__':
    app.run(port=5001, debug=True)
