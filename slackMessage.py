import json
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# # Replace these with your own values
slack_token = "xoxb-6000398059280-6401040416006-Bj3QltJsYs4qwKy6CH1dHBX6"



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
    
    
    emojiSpeaker = ":loudspeaker:"
    smily = ":blush:"
    url = "https://hooks.slack.com/services/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"
    
    client = WebClient(token=slack_token)
    channel_id = "#test_1"

    message = get_random_quote()
    title = (f"Update your daily status {emojiSpeaker}" )
    
    slack_data = {
        # "username": "Remainder",
        "icon_emoji": emojiSpeaker,
        "channel": channel_id,
        "attachments": [
            {
                "color": "#ac27fa",
                "fields": [
                    {
                        "title": title,
                        "value": (f"{message}, {smily} <!here>"),
                        "short": "false",
                    }
                ]
            }
        ]
    }
    
    byte_length = str(len(json.dumps(slack_data)))
    # print(slack_data)
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    # response = requests.post(client.chat_postMessage(slack_token, channel_id, slack_data), data=json.dumps(slack_data), headers=headers)
    response = client.chat_postMessage(channel=channel_id, text=title)
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
