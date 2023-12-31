# Slack Message Cleaner

This project allows you to delete your messages from Slack channels or direct messages. 

## Prerequisites

Before you begin, ensure you have met the following requirements:

1. You have installed the latest version of [slack-cli](https://api.slack.com/automation/quickstart)
2. Your workspace is configured with the Slack API
3. You have created a new [slack app](https://api.slack.com/apps)

## Configuring Slack Api

1. Navigate to https://api.slack.com/apps/YOUR-APP-ID-HERE/oauth? to copy your User OAuth Token and set user token scopes to include the following permissions:
    - channels:history
    - channels:read
    - channels:write
    - chat:write
    - groups:history
    - groups:read
    - im:history
    - im:read
    - mpim:history
    - mpim:read
2. Go to your Slack profile
3. Copy your token and user_id to creds.json

## Running Slack Message Cleaner

To run Slack Message Cleaner, follow these steps:

1. Open your terminal
2. Run the following command: `python main.py`
