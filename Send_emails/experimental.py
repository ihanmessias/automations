import PySimpleGUI as sg
from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

# Função para enviar o email
def send_email(email_origin, email_destiny, email_password, email_subject, email_body, attachment_path):
    try:
        # Código para enviar o email
        msg = EmailMessage()
        msg['From'] = email_origin
        msg['To'] = email_destiny
        msg['Subject'] = email_subject

        msg.set_content(email_body, subtype='html')

        if attachment_path:
            mime_type, mime_subtype = mimetypes.guess_type(attachment_path)[0].split('/')
            with open(attachment_path, 'rb') as attachment:
                msg.add_attachment(attachment.read(), maintype=mime_type,
                                   subtype=mime_subtype, filename=attachment_path)

        safe = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', '465', context=safe) as smtp:
            smtp.login(email_origin, email_password)
            smtp.sendmail(email_origin, email_destiny, msg.as_string())

        sg.popup('Email enviado com sucesso!')
    except smtplib.SMTPAuthenticationError:
        sg.popup('Erro de autenticação. Verifique a senha do email.')

# Layout da interface gráfica
layout = [
    [sg.Text('Email de Origem:'), sg.Input(key='email_origin')],
    [sg.Text('Email(s) de Destino (separados por vírgula):'), sg.Input(key='email_destiny')],
    [sg.Text('Senha do Email de Origem:'), sg.Input(key='email_password', password_char='*')],
    [sg.Text('Assunto:'), sg.Input(key='email_subject')],
    [sg.Text('Caminho do Anexo (opcional):'), sg.Input(key='attachment_path'), sg.FileBrowse()],
    [sg.Text('Template HTML:'), sg.Input(key='template_path'), sg.FileBrowse()],
    [sg.Button('Enviar Email'), sg.Button('Limpar')]
]

# Criação da janela
window = sg.Window('Enviar Email', layout)

# Loop de eventos da janela
while True:
    event, values = window.read()

    # Verifica se a janela foi fechada
    if event == sg.WINDOW_CLOSED:
        break

    # Verifica se o botão "Enviar Email" foi clicado
    if event == 'Enviar Email':
        # Coleta os valores dos campos
        email_origin = values['email_origin']
        email_destiny = [email.strip() for email in values['email_destiny'].split(',')]
        email_password = values['email_password']
        email_subject = values['email_subject']
        attachment_path = values['attachment_path']
        template_path = values['template_path']

        # Lê o conteúdo do template HTML
        with open(template_path, 'r', encoding='utf-8') as template_file:
            email_body = template_file.read()

        # Chama a função send_email
        send_email(email_origin, email_destiny, email_password, email_subject, email_body, attachment_path)

    # Verifica se o botão "Limpar" foi clicado
    if event == 'Limpar':
        window['email_origin'].update('')
        window['email_destiny'].update('')
        window['email_password'].update('')
        window['email_subject'].update('')
        window['attachment_path'].update('')
        window['template_path'].update('')

# Fecha a janela ao finalizar
window.close()