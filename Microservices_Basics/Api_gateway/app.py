from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ROUTES = {
    'users': 'http://user_service:5000',
    'orders': 'http://order_service:5001'
}

@app.route('/<service>/<path:path>', methods=['GET', 'POST'])
def gateway(service, path):
    if service not in ROUTES:
        return jsonify({"error": "Service not found"}), 404

    url = f"{ROUTES[service]}/{path}"
    
    if request.method == 'GET':
        response = requests.get(url)
    elif request.method == 'POST':
        response = requests.post(url, json=request.json)
    
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)