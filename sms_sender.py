# importing the client from twilio
from twilio.rest import Client
import values
# instantiating the Client


def send_sms(message):
    account_sid = values.twilio_account_sid
    auth_token = values.twilio_auth_token
    client = Client(account_sid, auth_token)
    # sending message
    try:
        message = client.messages.create(
            body=message,
            from_="+19894593490",
            to="+256789748424")
    except:
        print("Failed to send message")


if __name__ == '__main__':
    send_sms("This is the default message")
