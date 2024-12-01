import redis # type: ignore
import json
import boto3 # type: ignore

# Redis connection
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Configure Amazon SES or any email service
ses_client = boto3.client("ses", region_name="us-east-1")

def process_notifications():
    while True:
        notification = redis_client.rpop("notifications")
        if notification:
            data = json.loads(notification)
            send_email(data["customer_email"], data["status"], data["package_id"])

def send_email(to_email, status, package_id):
    subject = f"Update on your package {package_id}"
    body = f"Your package is currently: {status}."
    ses_client.send_email(
        Source="your-email@example.com",
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}},
        },
    )

if __name__ == "__main__":
    process_notifications()
