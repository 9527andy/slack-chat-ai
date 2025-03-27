from slack_sdk.errors import SlackApiError
from ai.providers import get_gemini_prodiver_response
from constants.constant import BLOCK_MESSAGE


def app_block_message(channel, thread, user, client, logger):
    try:
        client.chat_postMessage(
            channel=channel, thread_ts=thread, username=user, blocks=BLOCK_MESSAGE
        )
    except SlackApiError as e:
        logger.error(f"Error sending message: {e}")
    except Exception as e:
        logger.error(f"Error sending message: {e}")
