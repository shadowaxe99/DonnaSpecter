```python
import os
import requests
from datetime import datetime
from msal import ConfidentialClientApplication

# Load user credentials and email from environment variables
USER_CREDENTIALS = os.getenv("USER_CREDENTIALS")
USER_EMAIL = os.getenv("USER_EMAIL")

# Initialize MSAL client application
client_app = ConfidentialClientApplication(
    USER_CREDENTIALS["client_id"],
    authority=USER_CREDENTIALS["authority"],
    client_credential=USER_CREDENTIALS["client_secret"],
)

# Define scopes for Microsoft Graph API
SCOPES = ["https://graph.microsoft.com/.default"]

# Function to get access token
def get_access_token():
    result = None
    result = client_app.acquire_token_silent(SCOPES, account=None)

    if not result:
        result = client_app.acquire_token_for_client(SCOPES)

    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception(result.get("error_description"))

# Function to schedule a task
def schedule_task(task):
    # Get access token
    access_token = get_access_token()

    # Define endpoint and headers
    endpoint = f"https://graph.microsoft.com/v1.0/users/{USER_EMAIL}/calendar/events"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Define event body
    event_body = {
        "subject": task["subject"],
        "start": {
            "dateTime": task["start_time"].isoformat(),
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": task["end_time"].isoformat(),
            "timeZone": "UTC"
        },
        "body": {
            "contentType": "text",
            "content": task["description"]
        }
    }

    # Send POST request to create a new event
    response = requests.post(endpoint, headers=headers, json=event_body)

    # Check response status
    if response.status_code == 201:
        print(f"Task '{task['subject']}' has been scheduled successfully.")
    else:
        print(f"Failed to schedule task '{task['subject']}'. Error: {response.text}")
```