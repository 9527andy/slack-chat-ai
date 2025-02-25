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
    try:
        user_message = message["text"]
        data = {"message": user_message}

        response = requests.post(API_URL, json=data, headers=HEADER)
        response.raise_for_status()
        model_reply = response.json()
        say(model_reply["textResponse"])
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        say("Sorry, I'm having trouble connecting to the AI. Please try again later.")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        say("Something went wrong. Please try again later.")
