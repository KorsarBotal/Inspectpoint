from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

INSPECTPOINT_API_KEY = "gBohTUH7C7eelWa3RCiUeOjcVtSJ8hOY"
INSPECTPOINT_API_URL = "https://api.inspectpoint.com/v2/inspections"

@app.route("/submit", methods=["POST"])
def proxy():
    data = request.json
    headers = {
        "Authorization": f"Bearer {INSPECTPOINT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(INSPECTPOINT_API_URL, headers=headers, json=data)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
