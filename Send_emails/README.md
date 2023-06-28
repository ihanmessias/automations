# ✉️ Send Emails
Este script foi desenvolvido para automatizar o envio de e-mails de forma segura, utilizando protocolos de segurança e permitindo o envio de anexos. Ele foi construído em formato de template, o que permite que seja facilmente personalizado e adaptado às suas necessidades específicas.

# 🔧 Notas:
Esse script em Python é usado para enviar um email utilizando a biblioteca smtplib e a classe EmailMessage do módulo email.message. Vou explicar cada passo do script e comentar sobre cada parâmetro usado:

## Importação de bibliotecas:

```python
from email.message import EmailMessage
import smtplib
import ssl
import mimetypes
```

Nessa seção, as bibliotecas necessárias para enviar emails e lidar com anexos são importadas. A classe EmailMessage é usada para criar e manipular mensagens de email, smtplib é usada para enviar emails através do protocolo SMTP (Simple Mail Transfer Protocol), ssl é usado para criar um contexto seguro para a conexão SMTP e mimetypes é usado para determinar o tipo de conteúdo de um arquivo.

## Configuração:

```python
email_pass = open('./conf/pass.conf', 'r').read()
email_origin = 'emaildeenvio@gmail.com'
email_destiny = ['emaildedestino@gmail.com']
```

Nessa seção, são definidas as configurações do email, como a senha para autenticação, o endereço de email de origem e o(s) endereço(s) de email de destino. A senha é lida a partir de um arquivo pass.conf localizado no diretório `./conf/.`

*OBS:* Como cadastrar senha: https://support.google.com/mail/answer/185833?hl=pt-BR

## Template do Email:

```python
subject = 'Envio de Email utilizando Python'
body = open('./template/email.html', 'r').read()
```

Agora são definidos o assunto e o corpo do email. O assunto é uma string simples e o corpo é lido a partir de um arquivo email.html localizado no diretório ./template/. Esse arquivo contém o conteúdo HTML do email.

## Enviar o Email:

```python
msg = EmailMessage()
msg['From'] = email_origin
msg['To'] = email_destiny
msg['Subject'] = subject
```

Aqui, uma nova instância da classe EmailMessage é criada e os campos de cabeçalho do email são configurados, como o remetente (From), o(s) destinatário(s) (To) e o assunto (Subject).

## Anexar Arquivos:

```python
msg.set_content(body, subtype='html')
img_path = './archive/archive.zip'
mime_type, mime_subtype = mimetypes.guess_type(img_path)[0].split('/')
with open(img_path, 'rb') as attachment:
    msg.add_attachment(attachment.read(), maintype=mime_type,
                       subtype=mime_subtype, filename=img_path)
```
Por ultimo o conteúdo do email é definido usando o corpo lido anteriormente e especificando que o tipo de conteúdo é HTML. Em seguida, é anexado um arquivo ao email. No exemplo, é usado o arquivo `archive.zip` localizado no diretório `./archive/.` O tipo e o subtipo MIME são determinados usando a função mimetypes.guess_type a partir do caminho do arquivo. O arquivo é aberto no modo binário ('rb') e lido como bytes. Em seguida, é adicionado à mensagem usando o método add_attachment da instância msg, especificando o tipo MIME principal (maintype), o subtipo MIME (subtype) e o nome.

### 🤝 Suporte/Contato

[![LinkedIn Badge](https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=)](https://www.linkedin.com/in/ihanmessias/)
[![Whatsapp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/61996487935)
[![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/devlinuxtv/)

✉ ihanmessias.dev@gmail.com

<p align="center">Ihan Messias Nascimento Dos Santos</p>