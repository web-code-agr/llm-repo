import os
import requests

ACCESS_TOKEN = os.getenv("PSCHATACCESSTOKEN")
REQUEST_URL = os.getenv("PSCHAT_REQUEST_URL")

class ChatCompletion:

    def create(self, message: str, model="gpt4", temperature = 1.0):
        headersList = {
            "accept": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = f'{{"message":"{message}", "options": {{"model":"{model}", "temperature":"{temperature}"}}}}'
        response = requests.request("POST", REQUEST_URL+"/", data=payload,  headers=headersList)
        return response
