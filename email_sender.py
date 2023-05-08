import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email_text import html_format
from decouple import config
import base64
import json

# Informações do servidor SMTP e credenciais de login
smtp_server = config('SMTP_SERVER', default='smtp.gmail.com')
smtp_port = config('SMTP_PORT', default=587, cast=int)
smtp_username = config('SMTP_USERNAME', default='avandocampos@gmail.com')
smtp_password = config('SMTP_PASSWORD')

# Destinatário e assunto do e-mail
to_email = config('TO_EMAIL', default='avando.campos@sti.ufc.br')
email_subject = 'Gráficos dos testes de velocidade'
email_body = html_format

# Lê os dados do arquivo gerado pelo código anterior
with open('results.json', 'r') as json_file:
    results = json.load(json_file)

# Ler a imagem e converter para formato base64
with open('graph.png', 'rb') as f:
    img_data = f.read()
img_base64 = base64.b64encode(img_data).decode()

# Cria o objeto MIMEMultipart e adiciona o corpo do e-mail
msg = MIMEMultipart()
msg['Subject'] = email_subject
msg['To'] = to_email
msg.attach(MIMEText(email_body, 'html'))

# Cria o objeto MIMEImage com a imagem em formato base64
img = MIMEImage(base64.b64decode(img_base64))
img.add_header('Content-ID', '<graph>')
msg.attach(img)

# Conecta-se ao servidor SMTP e envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(smtp_username, to_email, msg.as_string())
