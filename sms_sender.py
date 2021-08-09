# importing the client from twilio
from twilio.rest import Client
account_sid = "ACe2cd91fbc77ea5404d176a3d2ccce312"
auth_token = "713c5e7282868268ec1d413777ffde24"
# instantiating the Client
client = Client(account_sid, auth_token)
# sending message
message = client.messages.create(body='Hi there! How are you?', from_="+16515046067", to="+256789748424")
# printing the sid after success
print(message.sid)
