
# Notification API

This project is a high-performance API to handle 10,000 notification requests per minute, using Mailgun's SMTP service for sending email notifications.

## Features
- Accepts client ID, customer email, and package status as input.
- Sends email notifications asynchronously to ensure non-blocking API performance.
- Supports Mailgun SMTP integration for reliable email delivery.
- Secure credential management using `.env` files.

## Requirements
- Python 3.8+
- `python-dotenv` for managing environment variables
- `fastapi` for building the API
- `smtplib` for sending emails
- `uvicorn` for running the API server

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/kanishka231/notifiction_api
cd notification-api
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Create a `.env` file in the root directory and add the following variables:
```env
SMTP_HOST=smtp.mailgun.org
SMTP_PORT=587
SMTP_USER=postmaster@sandbox8ac792fc3a834a67bfddfcc382207a07.mailgun.org
SMTP_PASS=c0ae0b5f3fcb9a6983d0a228e490a5be-f55d7446-627b9a98
```

### Step 4: Run the API
Start the API server using Uvicorn:
```bash
uvicorn main:app --reload
```

### Step 5: Test the API
Use a tool like Thunder Client or Postman to send a POST request to the endpoint:
```http
POST /send-notification/
Content-Type: application/json

{
  "client_id": "client123",
  "email": "example@domain.com",
  "package_status": "shipped"
}
```

## Deployment
For production deployment, consider using Docker or hosting services like AWS, Azure, or Google Cloud.

## License
This project is licensed under the MIT License.

---

**Note:** Free Mailgun accounts can only send emails to authorized recipients. Add recipient addresses in the Mailgun Account Settings to test the API.


