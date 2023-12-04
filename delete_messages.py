import os,json,time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

with open('creds.json', 'r') as file:
    creds = json.load(file)
token = creds['token']
user_id = creds['user_id']
client = WebClient(token=token)

def delete_my_messages(channel_id):
    print(f"Deleting from {channel_id}")
    try:
        delete_count = 0
        start_time = time.time()
        response = client.conversations_history(channel=channel_id)
        while True:
            user_messages = [message for message in response['messages'] if message.get('user') == user_id]
            for message in user_messages:
                print(message['text'])
                client.chat_delete(channel=channel_id, ts=message['ts'])
                delete_count += 1

                # Rate limit control (tweak for your needs)
                rate_limit = 22
                if delete_count % rate_limit == 0:
                    elapsed_time = time.time() - start_time
                    if elapsed_time < 60:
                        wait_time = 60 - elapsed_time
                        print(f"Rate limit approached, waiting for {wait_time} seconds...")
                        time.sleep(wait_time)
                    start_time = time.time()
            next_cursor = response['response_metadata']['next_cursor']
            if not next_cursor:
                break
            response = client.conversations_history(channel=channel_id, cursor=next_cursor)

        print(f"Messages deleted in channel {channel_id}: {delete_count}")

    except SlackApiError as e:
        print(f"Error: {e}")