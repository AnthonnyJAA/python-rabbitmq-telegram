import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)

token = "8832007035:AAH1lI3F3GSmv7nr8Ig104odJCzTX-2ya9k"
chat_id = -1003741808146
message = "Ola Mundo"

send_telegram_message(token, chat_id, message)