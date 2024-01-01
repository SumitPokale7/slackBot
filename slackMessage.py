import json
import requests

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
    # url = "https://hooks.slack.com/services/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"
    # url = "https://hooks.slack.com/services/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"
    url = "https://hooks.slack.com/services/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"

    
    message = get_random_quote()
    title = (f"Update your daily status {emojiSpeaker}" )
    
    slack_data = {
        "username": "Remainder",
        "icon_emoji": emojiSpeaker,
        "channel": "#daily-status",
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
    print(slack_data)
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    
    if response.status_code != 200:
        print(response.text)
        raise Exception(response.status_code, response.text)
    
    
