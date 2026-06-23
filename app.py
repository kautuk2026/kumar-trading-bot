from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("8843764106:AAET5Nlvp-lcWQKHRsCOzgIgQNKqslObl2o")
CHAT_ID = os.environ.get("917384025")

@app.route("/")
def home():
    return "Kumar Trading Bot Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    message = data.get(
        "message",
        "🚀 New Trading Signal"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
