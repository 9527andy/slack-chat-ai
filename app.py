from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

api_url = "http://localhost:3001/api/v1/workspace/jader/chat"
api_key = os.environ["ANYTHINGLLM_API_KEY"]
header ={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("message")
def handle_message_events(message, say, logger):
    print(message)
    user_message = message["text"]
    data =  {
        "message": user_message,
        "mode": "chat"
        }
    print(user_message)

    response = requests.post(api_url, json=data, headers=header)
    if response.status_code == 200:
        model_reply = response.json()
        say(model_reply["textResponse"])
    else:
        print(f"handle message events failed: {response.status_code}，error: {response.text}")

@app.event("app_mention")
def handle_app_mention_events(event, say, logger):
    print(event)
    user_message = event["text"]
    data =  {
        "message": user_message,
        "mode": "chat"
        }
    print(user_message)

    response = requests.post(api_url, json=data, headers=header)
    if response.status_code == 200:
        model_reply = response.json()
        say(model_reply["textResponse"])
    else:
        print(f"handle message events failed: {response.status_code}，error: {response.text}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
