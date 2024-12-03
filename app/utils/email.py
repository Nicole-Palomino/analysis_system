from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings    

import smtplib

def send_verification_email(email: str, token: str):
    message = MIMEMultipart()
    message["Subject"] = "Verify Your Email"
    message["From"] = settings.SMTP_EMAIL
    message["To"] = email

    link = f"http://localhost:8000/verify-email?token={token}"
    body = f"Click the link to verify your email: {link}"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_EMAIL, email, message.as_string())

def send_reset_password_email(email: str, token: str):
    message = MIMEMultipart()
    message["Subject"] = "Recuperación de Contraseña"
    message["From"] = settings.SMTP_EMAIL
    message["To"] = email

    link = f"http://localhost:8000/reset-password?token={token}"
    body = f"Haz clic en el siguiente enlace para restablecer tu contraseña: {link}"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_EMAIL, email, message.as_string())
        