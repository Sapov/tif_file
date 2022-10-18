import smtplib
import os
from email.mime.text import MIMEText


def send_email(message):
    sender = 'sapov@mail.ru'
    password= os.getenv("EMAIL_PASSWORD")
    server = smtplib.SMTP('smtp.')