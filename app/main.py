from fastapi import FastAPI, HTTPException
from app.models import NotificationRequest
from app.managers.notification_manager import NotificationManager

app = FastAPI()

# Initialize NotificationManager
notification_manager = NotificationManager()

@app.post("/send-notification/")
async def send_notification(request: NotificationRequest):
    try:
        await notification_manager.send_notification(
            channel=request.channel,
            recipient=request.recipient,
            message=request.message,
            package_status=request.package_status,
        )
        return {"message": f"Notification for {request.recipient} via {request.channel} is being processed."}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

