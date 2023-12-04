import os, json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


with open('creds.json', 'r') as file:
    creds = json.load(file)
TOKEN = creds['token']
client = WebClient(token=TOKEN)

def get_channels_with_my_messages(user_id):
    channels_with_messages = []

    try:
        channels_result = client.conversations_list()
        for channel in channels_result['channels']:
            channel_id = channel['id']
            messages_result = client.conversations_history(channel=channel_id)
            for message in messages_result['messages']:
                if 'user' in message and message['user'] == user_id:
                    channels_with_messages.append(channel['id'])
                    break

    except SlackApiError as e:
        print(f"Error: {e}")

    return channels_with_messages

def list_dm_conversations():
    try:
        response = client.users_conversations(types='im')
        dm_ids = [conversation['id'] for conversation in response['channels']]
        return dm_ids

    except SlackApiError as e:
        print(f"Error: {e}")
        return []