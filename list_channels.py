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
        im_channels = client.users_conversations(types=['im'])
        mpim_channels  = client.users_conversations(types=['mpim'])
        dm_ids = [conversation['id'] for conversation in im_channels['channels']]
        dm_users = [conversation['user'] for conversation in im_channels['channels']]
        mpim_ids = [conversation['id'] for conversation in mpim_channels['channels']]
        mpim_users = [conversation['name'] for conversation in mpim_channels['channels']]
        dm_names = []
        for user in dm_users:
            reference = client.users_info(user=user)
            dm_names.append(reference['user']["profile"]["real_name"])
        return dm_ids.append(mpim_ids)

    except SlackApiError as e:
        print(f"Error: {e}")
        return []