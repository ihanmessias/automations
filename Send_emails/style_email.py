from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

email_pass = open('./config/pass.conf', 'r').read()
email_origin = 'ihanmessias.dev@gmail.com'
email_destiny = ['ihanmessiassantos@gmail.com']

subject = 'Envio de Email utilizando Python'
body = open('./template/email_template.html', 'r').read()

msg = EmailMessage()
msg['From'] = email_origin
msg['To'] = email_destiny
msg['Subject'] = subject

msg.set_content(body, subtype='html')

attachment_path = './archive/archive.zip'
mime_type, mime_subtype = mimetypes.guess_type(attachment_path)[0].split('/')
with open(attachment_path, 'rb') as attachment:
    msg.add_attachment(attachment.read(), maintype=mime_type,
                       subtype=mime_subtype, filename=attachment_path)

safe = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', '465', context=safe) as smtp:
    smtp.login(email_origin, email_pass)
    # smtp.sendmail(email_origin, email_destiny, msg.as_string())
    smtp.send_message(msg)