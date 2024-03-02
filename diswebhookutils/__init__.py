import requests

def send_webhookmsg(weburl, content, username):
    data = {
        "content" : content,
        "username" : username
    }

    try:
        result = requests.post(weburl, json = data)
        result.raise_for_status()
        print("MESSAGE SENT WITH SUCCESS")
    except Exception as e:
        print(f"ERROR WHILE SENDING WEBHOOK MESSAGE: {e}")

def send_webhookembed(weburl, content, title, username):
    data = {
        "content" : content,
        "username" : username
    }

    data["embeds"] = [
        {
            "description" : content,
            "title" : title
        }
    ]

    try:
        result = requests.post(weburl, json = data)
        result.raise_for_status()
        print("MESSAGE SENT WITH SUCCESS")
    except Exception as e:
        print(f"ERROR WHILE SENDING WEBHOOK MESSAGE: {e}")