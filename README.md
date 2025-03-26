# slack-chat-ai
This app will communicate with Anything LLM, If the user sends a question to slack-chat-ai, slack-chat-ai will respond based on the knowledge bank in Anything LLM
# pre-condition
## The Anything LLM builds up a Gemini AI model and a default workspace.

## Build up a Slack app at https://api.slack.com/apps
1. Create a new app
1. From Scratch
1. OAuth & Permissions
   1. Bot Token Scopes -> chat:write, chat:write:public
   2. OAuth Tokens for Your Workspace - > Install to Workspace
   3. OAuth Tokens for Your Workspace -> save Bot User OAuth Tokens value
1. Basic Info
   1. App-Level Tokens - > Generate an app-level token -> Scope -> connections:write
   2. App-Level Tokens - > Generate an app-level token -> save App-Level Tokens value
1. Socket Mode
   1. Connect using Socket Mode - > Enable Socket Mode -> On
1. Interactivity Shortcuts
   1. Interactivity -> On
1. Event Subscriptions
   1. Enable Events - > On
   2. Subscribe to bot events - > app_mention, message:groups, message:im
1. App Home
   1. Show Tabs - > Message Tab - > On
   2. Show Tabs - > Message Tab - > Allow users to send Slash commands and messages from the message tab
  
## Anything LLM setup

`
export STORAGE_LOCATION=$HOME/anythingllm && \
mkdir -p $STORAGE_LOCATION && \
touch "$STORAGE_LOCATION/.env" && \
docker run -d -p 3001:3001 \
--cap-add SYS_ADMIN \
-v ${STORAGE_LOCATION}:/app/server/storage \
-v ${STORAGE_LOCATION}/.env:/app/server/.env \
-e STORAGE_DIR="/app/server/storage" \
mintplexlabs/anythingllm
`

## Python environment setup 
1. New Python visual environment
   
   `find . -type d -name "bin" | grep -E "/[^/]+/bin$" | sed 's/\/bin$//'`
   
   `python3 -m venv slack-chat-ai`
   
   `source slack-chat-ai/bin/activate`
1. Install necessary lib
   
  `pip3 install slack_bolt`

  `pip3 install python-dotenv`

  `pip3 install requests`
