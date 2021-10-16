# importing the client from twilio
from twilio.rest import Client
import config
# instantiating the Client
def send_sms(message):
    account_sid = config.twilio_account_sid
    auth_token = config.twilio_auth_token
    client = Client(account_sid, auth_token)
    # sending message
    message = client.messages.create(
        body=message,
        from_="+15405023047",
        to="+256789748424")
   
    

if __name__ == '__main__':
    send_sms("This is the default message")
    