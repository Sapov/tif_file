import smtplib
from email.mime.text import MIMEText
from email.header import Header
from ya_token import gmail_pass


def send_mail(message: str, subject: str):
    email = 'rpk.reds@gmail.com'  # ОТ КОГО
    password = gmail_pass
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


