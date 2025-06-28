# app.py
from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def forward_message():
    data = request.json
    message = data.get("message", "")
    
    if not message:
        return {"error": "No message provided"}, 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"Proxy: {message}"}
    requests.post(url, data=payload)

    return {"status": "sent"}, 200

@app.route("/", methods=["GET"])
def home():
    return "Telegram Proxy is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
