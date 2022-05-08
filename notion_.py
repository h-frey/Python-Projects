from notion.client import NotionClient
import pyttsx3 as speaker
import random
import config
from email_send import send_email
from sms_sender import send_sms



# def notify(message):
    # """makes notification on the desktop"""
    # notify = ToastNotifier()
    # notify.show_toast("Notion Reads", message, duration=20, threaded=True)

def speak(message):
    """Reads the message out loud via desktop"""
    speak = speaker.init()
    speak.setProperty("rate", 150)
    speak.say(message)
    speak.runAndWait()

def get_message():
    """Connect to the notion api and fetch message"""
    token = "10dc9ff667414ee73589d7a9ec548dea526bf85e15a6e2d1f701df3ba4814142dfee311ff9f4ff86422126ccb41ee33bb067d809b84dd8107a43a34827a38218064961988ff817c86e6ee91a7ef6"
    client = NotionClient(token_v2=token)
    page = client.get_block("aa06e7c5bf104d3eb4c10a7d2e011300e")
    page_elements = page.children
    random_block = random.choice(page_elements)

    if random_block.type == "text":
        message = random_block.title
        return message
    else:
         return get_message()

# try:
message = get_message()
# notify(message)
speak(message)
send_email(message)
send_sms(message)

# except:
    # print("Error Occurred")
    # input()





