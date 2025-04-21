import requests
import json

def send_telegram_message(message: str):
    with open("config/telegram_config.json") as f:
        config = json.load(f)
        
    token = config["TELEGRAM_TOKEN"]
    chat_id = config["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Telegram Error: {e}")
