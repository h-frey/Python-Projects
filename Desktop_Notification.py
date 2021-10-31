from win10toast import ToastNotifier
import time
from plyer import notification
import pyttsx3 as speaker
from email_send import send_email

#this is an example of a change 
""" Original ideas for this program included the following
1. Grab the weekly plan, quote, or whatever from a .txt file or a notion page( saves you from writing the file locally and works automatically online)
2. Send it to the desktop and read it out loud at a particular time of day preferably morning or the first time you open your pc
3. Send it to your email address 
4. Finally, send it via text message and now let us see how you will not get the notification"""
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