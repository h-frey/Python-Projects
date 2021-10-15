from notion.client import NotionClient
import pyttsx3 as speaker
from win10toast import ToastNotifier
from random import randint
import config
from email_send import send_email


def notification(message):
    """makes notification on the desktop"""
    notify = ToastNotifier()
    notify.show_toast("Notion Reads", message, duration=20)


def read_out_loud(message):
    """Reads the message out loud via desktop"""
    speak = speaker.init()
    speak.setProperty("rate", 150)
    speak.say(message)
    speak.runAndWait()

try:
    token = config.notion_v2
    client = NotionClient(token_v2=token)
    page = client.get_block(config.notion_site)
    page_elements = page.children
    item_number = randint(0, len(page_elements))
    message = page_elements[item_number].title
    
    notification(message)
    read_out_loud(message)
    send_email(message)

except:
    print("An error occurred")





