import os

API_URL = os.environ["ANYTHINGLLM_WORKSPACE_URL"]
API_KEY = os.environ["ANYTHINGLLM_API_KEY"]
HEADER ={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

