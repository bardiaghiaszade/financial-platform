import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(receiver, first_name):
    message = EmailMessage()

    message["Subject"] = "Welcome to Financial Platform!"
    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver

    html = f"""
    <html>
        <body>
            <p>Hi {first_name},</p>

            <p>Welcome to Financial Platform!</p>

            <img src="https://media1.tenor.com/m/lCZ8PORtg0IAAAAd/spongebob-dance.gif"
                 alt="Welcome GIF">

        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)