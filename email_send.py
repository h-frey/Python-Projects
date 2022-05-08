from email import message
import smtplib
import ssl
import values


def send_email( message="default message"):
    """Send the email to my email : The subject should be included as subject: and message should be put as parameter"""
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "hnyanzi320@gmail.com"
    receiver_email = "hnyanzi32@gmail.com"
    password = values.gmail_password
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except:
            print("Email couldn't be sent!!!")

if __name__ == '__main__':
    send_email("This is the default message.")