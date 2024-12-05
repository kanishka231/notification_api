# app/managers/notification_manager.py

from app.services.email_service import EmailNotificationService
from app.services.mock_email_service import MockEmailNotificationService
from app.services.notification_service import NotificationService
from typing import Optional

class NotificationManager:
    def __init__(self, use_mock_email: bool = False):
        # Register available services
        if use_mock_email:
            self.services = {
                "email": MockEmailNotificationService(),
            }
        else:
            self.services = {
                "email": EmailNotificationService(),
                # "sms": SMSNotificationService(),  # Placeholder
                # "whatsapp": WhatsAppNotificationService(),  # Placeholder
            }

    async def send_notification(self, channel: str, recipient: str, message: Optional[str] = None, package_status: Optional[str] = None):
        """
        Sends a notification using the specified channel.
        """
        service: NotificationService = self.services.get(channel)
        if not service:
            raise ValueError(f"Notification channel '{channel}' is not supported.")
        
        # Call the send method with channel-specific parameters
        if channel == "email":
            await service.send(recipient=recipient, message=message or f"Your package status is: {package_status}")
        else:
            await service.send(recipient=recipient, message=message)