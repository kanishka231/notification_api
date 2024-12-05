# app/services/mock_email_service.py

from app.services.notification_service import NotificationService

class MockEmailNotificationService(NotificationService):
    async def send(self, recipient: str, message: str):
        # Log the email instead of sending it
        print(f"[MOCK EMAIL] Sending to {recipient}: {message}")