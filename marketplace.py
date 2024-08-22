from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Data Dummy
general_token = "MARKETPLACE-TOKEN-XXX"

# APIs
apis = {
    1: {  # id api di sini adalah integer
        "url": "http://localhost:5001/api/a",
        "token": "TOKEN-SELLER-A"
    },
    2: {
        "url": "http://localhost:5001/api/b",
        "token": "TOKEN-SELLER-B"
    },
    3: {
        "url": "http://localhost:5001/api/a/1",
        "token": "TOKEN-SELLER-A"
    },
    4: {
        "url": "http://localhost:5001/api/a/1",
        "token": "TOKEN-SELLER-A"
    }
}

# Purchases
purchases = {
    "PUR-XXX-001": {
        "api_id": 1,
        "amount": 100,
        "method": "GET"
    },
    "PUR-XXX-002": {
        "api_id": 2,
        "amount": 200,
        "method": "GET"
    },
    "PUR-XXX-003": {
        "api_id": 1,
        "amount": 300,
        "method": "POST"
    },
    "PUR-XXX-004": {
        "api_id": 1,
        "amount": 400,
        "method": "PUT"
    },
    "PUR-XXX-005": {
        "api_id": 1,
        "amount": 500,
        "method": "DELETE"
    },
}

# Marketplace API with token and purchaseID/PUR-XXX-001
@app.route('/api/purchase', methods=['GET'])
def purchase():
    try:
        token = request.headers.get('Authorization')
        if token != f"Bearer {general_token}":
            return jsonify({"error": "Invalid token"}), 401

        purchase_id = request.headers.get('X-PURCHASE-ID')
        if purchase_id not in purchases:
            return jsonify({"error": "Invalid purchase ID"}), 400

        purchase = purchases[purchase_id]
        api_id = purchase["api_id"]
        api = apis.get(api_id)
        if not api:
            return jsonify({"error": "API not found"}), 404

        response = requests.get(api["url"], headers={
            "Authorization": f"Bearer {api['token']}"
        })

        return jsonify(response.json()), response.status_code
    except Exception as e:
        # with error message
        return jsonify({"error": str(e)}), 500

@app.route('/api/purchase', methods=['POST'])
def purchase_post():
    try:
        token = request.headers.get('Authorization')
        if token != f"Bearer {general_token}":
            return jsonify({"error": "Invalid token"}), 401

        purchase_id = request.headers.get('X-PURCHASE-ID')
        if purchase_id not in purchases:
            return jsonify({"error": "Invalid purchase ID"}), 400

        purchase = purchases[purchase_id]
        api_id = purchase["api_id"]
        api = apis.get(api_id)
        if not api:
            return jsonify({"error": "API not found"}), 404

        response = requests.post(api["url"], headers={
            "Authorization": f"Bearer {api['token']}"
        }, json=request.json)

        return jsonify(response.json()), response.status_code
    except Exception as e:
        # with error message
        return jsonify({"error": str(e)}), 500

# PUT
@app.route('/api/purchase', methods=['PUT'])
def purchase_put():
    try:
        token = request.headers.get('Authorization')
        if token != f"Bearer {general_token}":
            return jsonify({"error": "Invalid token"}), 401

        purchase_id = request.headers.get('X-PURCHASE-ID')
        if purchase_id not in purchases:
            return jsonify({"error": "Invalid purchase ID"}), 400

        purchase = purchases[purchase_id]
        api_id = purchase["api_id"]
        api = apis.get(api_id)
        if not api:
            return jsonify({"error": "API not found"}), 404

        response = requests.put(api["url"], headers={
            "Authorization": f"Bearer {api['token']}"
        }, json=request.json)

        return jsonify(response.json()), response.status_code
    except Exception as e:
        # with error message
        return jsonify({"error": str(e)}), 500

# DELETE
@app.route('/api/purchase', methods=['DELETE'])
def purchase_delete():
    try:
        token = request.headers.get('Authorization')
        if token != f"Bearer {general_token}":
            return jsonify({"error": "Invalid token"}), 401

        purchase_id = request.headers.get('X-PURCHASE-ID')
        if purchase_id not in purchases:
            return jsonify({"error": "Invalid purchase ID"}), 400

        purchase = purchases[purchase_id]
        api_id = purchase["api_id"]
        api = apis.get(api_id)
        if not api:
            return jsonify({"error": "API not found"}), 404

        response = requests.delete(api["url"], headers={
            "Authorization": f"Bearer {api['token']}"
        })

        return jsonify(response.json()), response.status_code
    except Exception as e:
        # with error message
        return jsonify({"error": str(e)}), 500

# Run the marketplace server
if __name__ == '__main__':
    app.run(port=5000, debug=True)
