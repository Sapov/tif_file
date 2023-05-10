import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
# from ya_token import gmail_pass, FROM_MAIL
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def send_mail(message: str, subject: str):
    email = os.getenv('FROM_MAIL')  # ОТ КОГО
    password = os.getenv('GMAIL_PASS')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    dest_email = 'rpk.reds@ya.ru'
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = email
    msg['To'] = dest_email
    # server.set_debuglevel(1)  # Необязательно; так будут отображаться данные с сервера в консол__и
    server.sendmail(email, dest_email, msg.as_string())
    server.quit()

