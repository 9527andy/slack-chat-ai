from slack_sdk.errors import SlackApiError
from ai.providers import get_gemini_prodiver_response

"""
Handles the event when the app is mentioned in a Slack channel, retrieves the conversation context,
and generates an AI response if text is provided, otherwise sends a default response
"""


def app_mentioned_callback(event, say, logger, client):
    channel = event.get("channel")
    thread = event.get("thread_ts")
    user = event.get("user")
    user_input = event.get("text")

    try:
        ai_response = get_gemini_prodiver_response(user_input)
        response = client.chat_postMessage(
            channel=channel,
            text=f"<@{user}> {ai_response}",
            thread_ts=thread,
            username=user,
        )
        print(response)
    except SlackApiError as e:
        logger.error(f"Error sending message: {e}")
    except Exception as e:
        logger.error(f"Error sending message: {e}")
