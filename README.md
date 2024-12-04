
# Notification API

This project is a Notification API built with FastAPI to send notifications via different channels such as Email, SMS, and WhatsApp. The API uses external services for sending notifications and is designed to be easily extensible for integrating other services in the future.

## Features
- Sends email notifications using Mailgun (or any email service).
- The code is structured to easily add more notification services like SMS and WhatsApp.
- Asynchronous, non-blocking email sending to handle high-volume requests.
- API requests are processed in a multi-threaded manner for better scalability.

## Installation

### Prerequisites
- Python 3.8 or later
- FastAPI
- Uvicorn
- Other dependencies listed in `requirements.txt`

### Steps to Set Up and Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/kanishka231/notifiction_api
    cd notifiction_api
    ```

2. **Set up a virtual environment**:
    If you haven't installed `virtualenv`, you can do so using pip:
    ```bash
    pip install virtualenv
    ```

    Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .env\Scriptsctivate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure the `.env` file**:
    - Create a `.env` file in the root of your project.
    - Add your Mailgun SMTP credentials in the `.env` file:
    ```
    SMTP_HOST=smtp.mailgun.org
    SMTP_PORT=587
    SMTP_USER=postmaster@sandbox8ac792fc3a834a67bfddfcc382207a07.mailgun.org
    SMTP_PASS=your_smtp_password
    ```

6. **Run the FastAPI app**:
    ```bash
    uvicorn app.main:app --reload
    ```

    The FastAPI app will start running on `http://127.0.0.1:8000`.

7. **Test the API**:
    - Use Thunder Client, Postman, or any HTTP client to test the API by sending a POST request to `http://127.0.0.1:8000/send-notification/` with the following JSON body:
    ```json
    {
      "client_id": "client123",
      "recipient": "abc@gmail.com",
      "channel": "email",
      "message": "Your package has been shipped.",
      "package_status": "shipped"
    }
    ```

    - The expected response will be:
    ```json
    {
      "message": "Notification for abc@gmail.com is being processed."
    }
    ```

8. **Verify the email notification**:
    - Check the recipient's email inbox to confirm the notification is delivered.

## Directory Structure

```
notification_api/
│
├── app/
│   ├── config.py          # Contains the configuration like SMTP settings
│   ├── main.py            # FastAPI app definition
│   ├── models.py          # Pydantic models for request validation
│   ├── services/          # Contains different notification services (Email, SMS, etc.)
│   ├── managers/          # Contains logic for managing notification services
│   └── tasks.py           # Contains the task to send emails in a non-blocking way
│
├── requirements.txt       # List of Python dependencies
└── .env                   # Environment variables for sensitive information
```

## Future Improvements
- Integrate other notification channels like SMS and WhatsApp.
- Implement rate-limiting to avoid abuse and ensure optimal performance under high load.
- Add authentication to secure the API endpoints.
- Create more flexible and reusable notification handling logic.

