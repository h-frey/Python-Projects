from notion.client import NotionClient
import pyttsx3 as speaker
from win10toast import ToastNotifier
from random import randint
import config

speak = speaker.init()
notify = ToastNotifier()

token = config.notion_v2
client = NotionClient(token_v2 = token)
page = client.get_block("https://www.notion.so/Daily-Messages-7d78bececdb246fc82d50b90d5f93d13")
page_elements = page.children

item_number = randint(0, len(page_elements))

message = page_elements[item_number].title

notify.show_toast("Notion Message", message, duration = 20)
speak.setProperty("rate",150)
speak.say(message)
speak.runAndWait()


