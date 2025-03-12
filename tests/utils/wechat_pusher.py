import requests

class WeChatPusher:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, content):
        payload = {"msgtype": "text", "text": {"content": content}}
        response = requests.post(self.webhook_url, json=payload)
        return response.status_code == 200