from email import message
import smtplib
import ssl
import config


def send_email( message="default message"):
    """Send the email to my email : The subject should be included as subject: and message should be put as parameter"""
    port = 465
    smtp_server = config.email_smtp_server
    sender_email = config.email_sender_email
    receiver_email = config.email_receiver_email
    password = config.email_password
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except:
            print("Email couldn't be sent!!!")

if __name__ == '__main__':
    send_email("This is the default message.")