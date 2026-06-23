from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 🔥 Telegram details (fixed)
BOT_TOKEN = 8843764106:AAG7glTqU5GTGt66DaNOt5GSgNNf6M0ukDo"
CHAT_ID = "917384025"


@app.route("/")
def home():
    return "Kumar Trading Bot Running 🚀"


@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    if request.method == "GET":
        return "Webhook is LIVE ✅"

    data = request.get_json(silent=True)

    # 🔥 DEBUG LOGS
    print("🔥 WEBHOOK HIT")
    print("DATA:", data)

    # default message
    message = "🚀 New Trading Signal"

    # if message comes from request
    if data and "message" in data:
        message = data["message"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        res = requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": message
        })

        # 🔥 RESPONSE LOGS
        print("STATUS:", res.status_code)
        print("RESPONSE:", res.text)

    except Exception as e:
        print("❌ ERROR:", str(e))

    return {"status": "success"}


# 🔥 FOR RENDER / LOCAL RUN
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
