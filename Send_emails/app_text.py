# ---- Import Libs ---- #
from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

# ---- Configuration ---- #
email_pass = open('./conf/pass.conf', 'r').read()
email_origin = 'ihanmessias.dev@gmail.com'
email_destiny = ['ihanmessiassantos@gmail.com']

# ---- Email template ---- #
subject = 'Envio de Email utilizando Python'
body = open('./template/email.txt', 'r').read()

msg = EmailMessage()
msg['From'] = email_origin
msg['To'] = email_destiny
msg['Subject'] = subject

msg.set_content(body)
safe = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', '465', context=safe) as smtp:
    smtp.login(email_origin, email_pass)
    smtp.sendmail(email_origin, email_destiny, msg.as_string())
