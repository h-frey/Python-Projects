# importing the client from twilio
from twilio.rest import Client
account_sid = "######"
auth_token = "#######"
# instantiating the Client
client = Client(account_sid, auth_token)
# sending message
message = client.messages.create(body='Hi there! How are you?', from_="#######", to="########")
# printing the sid after success
print(message.sid)
