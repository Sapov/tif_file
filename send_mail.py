import smtplib
from email.mime.text import MIMEText
from email.header import Header
from ya_token import yandex_login


def send_mail(message: str):
    email = 'rpk.reds@yandex.ru'  # ОТ КОГО
    password = yandex_login
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    subject = "Печать на баннере"
    dest_email = 'rpk.reds@gmail.com'
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header('Тема письма это печать баннера', 'utf-8')
    # login = email
    msg['From'] = email
    msg['To'] = dest_email

    # server.set_debuglevel(1)  # Необязательно; так будут отображаться данные с сервера в консоли
    server.sendmail(email, dest_email, msg.as_string())
    server.quit()
