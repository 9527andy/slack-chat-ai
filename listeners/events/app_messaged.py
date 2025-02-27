from slack_sdk.errors import SlackApiError
from ai.providers import get_gemini_prodiver_response

"""
Handles the event when the app is mentioned in a Slack channel, retrieves the conversation context,
and generates an AI response if text is provided, otherwise sends a default response
"""


def app_messaged_callback(message, say, logger, client):
    channel = message.get("channel")
    thread = message.get("thread_ts")
    user = message.get("user")
    user_input = message.get("text")

    try:
        ai_response = get_gemini_prodiver_response(user_input)
        response = client.chat_postMessage(
            channel=channel,
            text=ai_response,
            thread_ts=thread,
            username=user,
        )
    except SlackApiError as e:
        logger.error(f"Error sending message: {e}")
    except Exception as e:
        logger.error(f"Error sending message: {e}")
