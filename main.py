from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel, EmailStr # type: ignore
import redis # type: ignore
import json

app = FastAPI()

# Redis connection for queuing
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

class NotificationRequest(BaseModel):
    company_id: str
    customer_email: EmailStr
    package_id: str
    status: str

@app.post("/send-notification")
async def send_notification(request: NotificationRequest):
    try:
        # Push to Redis queue
        redis_client.lpush("notifications", json.dumps(request.dict()))
        return {"message": "Notification queued successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error queuing notification")
