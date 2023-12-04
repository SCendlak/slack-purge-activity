import json
import os
from slack_sdk import WebClient
from list_channels import get_channels_with_my_messages, list_dm_conversations
from delete_messages import delete_my_messages

with open('creds.json', 'r') as file:
    creds = json.load(file)
    user_id=creds['user_id']

def main():
        channels_ids = get_channels_with_my_messages(user_id)
        dm_conversation_ids = list_dm_conversations()
        #Comment out if you want to keep channels or direct messages
        for conversation_id in channels_ids:
            delete_my_messages(conversation_id)
        for conversation_id in dm_conversation_ids['dm_ids']:
            delete_my_messages(conversation_id)

main()