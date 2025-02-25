from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
from dotenv import load_dotenv
import os
from listeners import register_listeners

load_dotenv('.env')




app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

register_listeners(app)

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
