from slack_bolt import App
from listeners.events.app_mentioned import app_mentioned_callback
from listeners.events.app_messaged import app_messaged_callback
from listeners.events import register



def register_listeners(app):
    register(app)