from win10toast import ToastNotifier
import time
from plyer import notification
import pyttsx3 as speaker
from email_send import send_email
#this is an example of a change 
engine=speaker.init()
notify=ToastNotifier()
message="This is an example of text to speech in english, tell me Humphrey do you like it?"
send_email(message)
notify.show_toast("Notification",message,duration=20)
time.sleep(20)
engine.setProperty("rate",150)
engine.say(message)
engine.runAndWait()
notification.notify(title="Notification using Python",message=message,timeout=20)