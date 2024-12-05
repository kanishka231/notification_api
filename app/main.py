from fastapi import FastAPI, HTTPException
from app.models import NotificationRequest,NotificationBatchRequest
from app.managers.notification_manager import NotificationManager
import asyncio

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


@app.post("/send-batch-notification/")
async def send_batch_notification(request: NotificationBatchRequest):
    try:
        tasks = []
        for notification in request.notifications:
            tasks.append(notification_manager.send_notification(
                channel=notification.channel,
                recipient=notification.recipient,
                message=notification.message,
                package_status=notification.package_status,
            ))
        
        # Run all tasks concurrently
        await asyncio.gather(*tasks)
        return {"message": "All notifications are being processed."}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
