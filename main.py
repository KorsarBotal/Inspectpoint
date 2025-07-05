from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

INSPECTPOINT_API_KEY = "gBohTUH7C7eelWa3RCiUeOjcVtSJ8hOY"
INSPECTPOINT_API_URL = "https://api.inspectpoint.com/v2/inspections"

@app.route("/", methods=["GET"])
def hello():
    return "Service is running!"

@app.route("/submit", methods=["POST"])
def proxy():
    data = request.form.to_dict()  # ВАЖНО: получаем как form-data
    headers = {
        "Authorization": f"Bearer {INSPECTPOINT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(INSPECTPOINT_API_URL, headers=headers, json=data)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
