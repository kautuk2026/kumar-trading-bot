from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "8843764106:AAG7glTqU5GTGt66DaNOt5GSgNNf6M0ukDo"
CHAT_ID = "917384025"

@app.route("/")
def home():
    return "Kumar Trading Bot Running 🚀"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    if request.method == "GET":
        return "Webhook is LIVE ✅"

    data = request.get_json(silent=True)

    message = "🚀 New Trading Signal"
    if data and "message" in data:
        message = data["message"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": message
        })
    except:
        pass

    return {"status": "success"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
