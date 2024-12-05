import aiosmtplib
from email.mime.text import MIMEText
from app.services.notification_service import NotificationService
from app.config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS

class EmailNotificationService(NotificationService):
    async def send(self, recipient: str, message: str):
        subject = "Notification Service"
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = recipient

        try:
            # Create an SMTP client session object
            async with aiosmtplib.SMTP(hostname=SMTP_HOST, port=SMTP_PORT, start_tls=True) as server:
                await server.login(SMTP_USER, SMTP_PASS)
                await server.send_message(msg)
            print(f"Email sent successfully to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")
            raise