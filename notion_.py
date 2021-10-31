from notion.client import NotionClient
import pyttsx3 as speaker
from win10toast import ToastNotifier
import random
import config
from email_send import send_email
from sms_sender import send_sms



def notify(message):
    """makes notification on the desktop"""
    notify = ToastNotifier()
    notify.show_toast("Notion Reads", message, duration=20, threaded=True)

def speak(message):
    """Reads the message out loud via desktop"""
    speak = speaker.init()
    speak.setProperty("rate", 150)
    speak.say(message)
    speak.runAndWait()

def get_message():
    """Connect to the notion api and fetch message"""
    token = config.notion_v2
    client = NotionClient(token_v2=token)
    page = client.get_block(config.notion_site)
    page_elements = page.children
    random_block = random.choice(page_elements)

    if random_block.type == "text":
        message = random_block.title
        return message
    else:
         return get_message()

try:
    message = get_message()
    notify(message)
    speak(message)
    send_email(message)
    send_sms(message)

except:
    print("Error Occurred")
    input()





