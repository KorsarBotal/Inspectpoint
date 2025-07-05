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
    data = request.form.to_dict() 
    print("Received from Tilda:", data)
    headers = {
        "Authorization": f"Bearer {INSPECTPOINT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(INSPECTPOINT_API_URL, headers=headers, json=data)
    return jsonify(response.json()), response.status_code
