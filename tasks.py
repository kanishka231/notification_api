import smtplib
from email.mime.text import MIMEText
from threading import Thread
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS

def send_email(to_email: str, package_status: str):
    """
    Sends an email with the package status using Mailgun SMTP.
    """
    subject = "Package Status Update"
    body = f"Your package status is: {package_status}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()  # Enable TLS encryption
            server.login(SMTP_USER, SMTP_PASS)  # Login using Mailgun credentials
            server.sendmail(SMTP_USER, to_email, msg.as_string())  # Send email
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def send_email_threaded(to_email: str, package_status: str):
    """
    Sends an email in a separate thread to handle high-volume requests.
    """
    Thread(target=send_email, args=(to_email, package_status)).start()
