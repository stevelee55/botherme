
# from smtplib import SMTP
import smtplib, ssl


port = 465  # for SSL

sender_email = "botherme.notifier@gmail.com"
password = "letsrockthis1!"

receiver_email = "yjheo@umich.edu"
# receiver_email = input("Receiver_email: ")

# message = input("message content (first line has to start with 'Subject: ' then have an empty line: ")

message = """\
Subject: Botherme Notification

Hey do ur stuff bruh"""

# Create a secure SSL context
context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login("botherme.notifier@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
