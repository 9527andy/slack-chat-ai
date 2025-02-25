from logging import Logger
from slack_sdk import WebClient
from slack_bolt import Say
import requests
import os
from constants.constant import API_URL
from constants.constant import HEADER

"""
Handles the event when the app is mentioned in a Slack channel, retrieves the conversation context,
and generates an AI response if text is provided, otherwise sends a default response
"""

def app_messaged_callback(message, say, logger):
    print(message)
    user_message = message["text"]
    data =  {
        "message": user_message,
        "mode": "chat"
        }
    print(user_message)

    response = requests.post(API_URL, json=data, headers=HEADER)
    if response.status_code == 200:
        model_reply = response.json()
        say(model_reply["textResponse"])
    else:
        print(f"handle message events failed: {response.status_code}，error: {response.text}")