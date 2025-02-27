from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from listeners import register_listeners
from constants.constant import TOKEN


app = App(token=TOKEN)

register_listeners(app)

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
