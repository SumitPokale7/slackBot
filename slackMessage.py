import json
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

url = os.environ.get('WEBHOOK_URL')
slack_token = "xoxb-6000398059280-6401040416006-9RWzbgkJ3TjlFqnydqCrqPxU"

print(url)

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        quote_data = response.json()
        return f'"{quote_data["content"]}" - {quote_data["author"]}'
    else:
        return "Failed to fetch a quote."

# print(get_random_quote())

if __name__ == '__main__':
    
    
    speakerEmoji = ":loudspeaker:"
    smilyEmoji = ":blush:"
    
    # url = "https://hooks.slack.com/services/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"
    
    # client = WebClient(token=slack_token)
    channel_id = "#test_1"

    # message = get_random_quote()
    title = (f"Update your daily status {speakerEmoji} \n {get_random_quote()}" )
    
    slack_data = {
        # "username": "Remainder",
        "icon_emoji": speakerEmoji,
        "channel": channel_id,
        "attachments": [
            {
                "color": "#ac27fa",
                "fields": [
                    {
                        "title": title,
                        "value": (f"{smilyEmoji} <!here>"),
                        "short": "false",
                    }
                ]
            }
        ]
    }
    
    # for the post message()
    # slack_data = {
    #     "icon_emoji": speakerEmoji,
    #     "channel": channel_id,
    #     "blocks": [
    #         {
    #             "type": "section",
    #             "block_id": "section1",
    #             "text": {
    #                 "type": "mrkdwn",
    #                 "text": f"*{title}*\n{get_random_quote()}, {smilyEmoji} <!here>"
    #             },
    #         }
    #     ]
    # }
    
    # print(slack_data)
    
    byte_length = str(len(json.dumps(slack_data)))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    # response = client.chat_postMessage(channel=channel_id, text=json.dumps(slack_data), headers=headers)
    
    if response.status_code != 200:
        print(response.text)
        raise Exception(response.status_code, response.text)
    
    
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError

# # Replace these with your own values
# slack_token = "YOUR_SLACK_TOKEN"
# channel_id = "YOUR_CHANNEL_ID"
# message_text = "Hello, this is a test message from Python!"

# def send_slack_message(token, channel, text):
#     client = WebClient(token=token)

#     try:
#         response = client.chat_postMessage(
#             channel=channel,
#             text=text
#         )
#         print("Message sent successfully:", response["ts"])
#     except SlackApiError as e:
#         print(f"Error sending message: {e.response['error']}")

# # Example usage
# send_slack_message(slack_token, channel_id, message_text)
