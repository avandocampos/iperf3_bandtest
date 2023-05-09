import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from decouple import config
import base64


def send_email(email_body, img_data):

    # Informações do servidor SMTP e credenciais de login
    smtp_server = config('SMTP_SERVER', default='smtp.gmail.com')
    smtp_port = config('SMTP_PORT', default=587, cast=int)
    smtp_username = config('SMTP_USERNAME', default='avandocampos@gmail.com')
    smtp_password = config('SMTP_PASSWORD')

    # Destinatário e assunto do e-mail
    to_email = config('TO_EMAIL', default='avando.campos@sti.ufc.br')
    email_subject = 'Gráficos dos testes de velocidade'

    # Converte a imagem para o formato base64
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


if __name__ == '__main__':
    from email_text import to_html
    import json

    with open('results.json', 'r') as json_file:
        results = json.load(json_file)

    email_body = to_html(results)

    with open('graph.png', 'rb') as img_file:
        img_data = img_file.read()

    send_email(email_body, img_data)
