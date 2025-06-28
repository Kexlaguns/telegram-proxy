from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    message = data.get("msg", "")
    if not message:
        return {"error": "No message provided"}, 400

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        requests.post(telegram_url, data=payload)
    except Exception as e:
        return {"error": str(e)}, 500

    return {"status": "sent"}
