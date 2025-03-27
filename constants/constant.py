import os

API_URL = os.environ["ANYTHINGLLM_WORKSPACE_URL"]
API_KEY = os.environ["ANYTHINGLLM_API_KEY"]
HEADER = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
TOKEN = os.environ.get("SLACK_BOT_TOKEN")


BLOCK_MESSAGE = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Does EISU Bot resolve your problem/issue?",
        },
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Yes"},
                "style": "primary",
                "value": "Yes",
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "No"},
                "style": "danger",
                "value": "No",
            },
        ],
    },
]
