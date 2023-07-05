```python
from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_message(to, body):
    message = client.messages.create(
        body=body,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )
    return message.sid

def make_call(to, url):
    call = client.calls.create(
        url=url,
        to=to,
        from_=TWILIO_PHONE_NUMBER
    )
    return call.sid

def receive_message(sid):
    message = client.messages.get(sid)
    return message.body

def receive_call(sid):
    call = client.calls.get(sid)
    return call.status
```