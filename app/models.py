from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class NotificationRequest(BaseModel):
    client_id: str = Field(..., description="Unique ID of the client making the request")
    recipient: str = Field(..., description="The recipient of the notification (email, phone, etc.)")
    channel: str = Field(..., description="Notification channel (email, sms, whatsapp)")
    message: Optional[str] = Field(None, description="Custom message for the notification")
    package_status: Optional[str] = Field(None, description="Status of the package (for email notifications)")

    class Config:
        schema_extra = {
            "example": {
                "client_id": "client123",
                "recipient": "kanishka@amigo.gg",
                "channel": "email",
                "message": "Your package has been shipped.",
                "package_status": "shipped"
            }
        }
