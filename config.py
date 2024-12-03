from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the environment variables
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))  # Convert to int as PORT is a number
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
