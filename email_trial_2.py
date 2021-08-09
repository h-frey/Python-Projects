import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465  # For SSL
password = "Humphrey@900"
smtp_server = "smtp.gmail.com"
sender_email = "hnyanzi320@gmail.com"
receiver_email = "hnyanzi32@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Last Python Sample"
message["From"] = sender_email
message["To"] = receiver_email


# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com
My name is Humphrey Nyanzi and I love Programming though I study
Sports Science at college.
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.<br>
       My name is Humphrey Nyanzi and I love Programming though I study Sports Science at college.
    </p>
    <input type="button" value="Click here">
  </body>
</html>
"""
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    try:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("email sent!")
    except:
        print("Could not login or send the mail.")
