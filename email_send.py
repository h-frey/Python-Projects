import smtplib,ssl



def send_email(message):
    """Insert the message you would like to send as a functional argument"""
    port=465 #For SSL
    password="Humphrey@900"
    smtp_server="smtp.gmail.com"
    sender_email="hnyanzi320@gmail.com"
    receiver_email="hnyanzi32@gmail.com"

    
    #Create a secure SSL context
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email,receiver_email,message)
            print("email sent!")
        except:
            print("Could not login or send the mail.")

