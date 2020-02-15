import os
import smtplib
import ssl

sender_email = os.getenv('SENDER_EMAIL')
receiver_email = os.getenv('RECEIVER_EMAIL')
password = os.getenv('EMAIL_PASSWORD')

def send_email(message_subject, message_body):
    """Send an email via Gmail SMTP Server"""

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    message = f"""\
    Subject: {message_subject}

    {message_body}

    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
