import os
from constants.constant import API_URL
from constants.constant import API_KEY
from constants.constant import HEADER
import requests
import logging
import google.api_core.exceptions

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class GeminiAI:

    def __init__(self):
        self.__ai_api_key = API_KEY
        self.__ai_url = API_URL

    def generate_ai_response(self, user_input):
        try:
            data = {"message": user_input, "mode": "query"}
            response = requests.post(self.__ai_url, json=data, headers=HEADER)
            response.raise_for_status()
            model_reply = response.json()
            return model_reply["textResponse"]
        except google.api_core.exceptions.Unauthorized as e:
            logger.error(f"Client is not Authorized. {e.reason}, {e.message}")
            raise e
        except google.api_core.exceptions.Forbidden as e:
            logger.error(f"Client Forbidden. {e.reason}, {e.message}")
            raise e
        except google.api_core.exceptions.TooManyRequests as e:
            logger.error(f"Too many requests. {e.reason}, {e.message}")
            raise e
        except google.api_core.exceptions.ClientError as e:
            logger.error(f"Client error: {e.reason}, {e.message}")
            raise e
        except google.api_core.exceptions.ServerError as e:
            logger.error(f"Server error: {e.reason}, {e.message}")
            raise e
        except google.api_core.exceptions.GoogleAPICallError as e:
            logger.error(f"Error: {e.reason}, {e.message}")
            raise e
        except google.api_core.exceptions.GoogleAPIError as e:
            logger.error(f"Unknown error. {e}")
            raise e