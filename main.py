from fastapi import FastAPI
from models import NotificationRequest
from tasks import send_email_threaded

app = FastAPI()

@app.post("/send-notification/")
async def send_notification(request: NotificationRequest):
    """
    API endpoint to send notification emails.
    """
    send_email_threaded(request.email, request.package_status)  # Non-blocking email sending
    return {"message": f"Notification for {request.email} is being processed."}

