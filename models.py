from pydantic import BaseModel, EmailStr

class NotificationRequest(BaseModel):
    client_id: str
    email: EmailStr
    package_status: str

