from email.message import EmailMessage
import ssl
import smtplib

email_sender = input("Enter Email For Sender: ").strip().lower()
email_password = input("Enter App Passwords: ").strip()

email_reciver = input("Enter Email For Reciver: ").strip().lower()

subject = input("Enter The Email Subject: ")

body = input("Enter The Email Body: ")


em = EmailMessage()

em['From'] = email_sender

em['To'] = email_reciver

em['subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
