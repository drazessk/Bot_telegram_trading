import requests
import time
from datetime import datetime
from telegram import Bot

# ==== CONFIGURATION ====
TOKEN = "8468135435:AAGaKhz-7LrUgj4oJOOeSkuC2IEYKwxUQR8"  # Ton token Telegram
CHAT_ID = "-1002596666061"  # ID de ton canal
INTERVAL = 900  # 900 secondes = 15 minutes

bot = Bot(token=TOKEN)

def get_gold_price():
    try:
        url = "https://www.goldapi.io/api/XAU/USD"
        headers = {
            "x-access-token": "goldapi-1g5u4qg90f6qpl-io",  # Token gratuit GoldAPI
            "Content-Type": "application/json"
        }
        r = requests.get(url, headers=headers)
        data = r.json()
        return data.get("price")
    except Exception as e:
        print("Erreur:", e)
        return None

def send_signal():
    price = get_gold_price()
    if price:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"📊 Signal XAU/USD\n💰 Prix actuel: {price} USD\n🕒 {now}"
    else:
        message = "⚠ Impossible de récupérer le prix de l'or."

    bot.send_message(chat_id=CHAT_ID, text=message)

while True:
    send_signal()
    time.sleep(INTERVAL)
