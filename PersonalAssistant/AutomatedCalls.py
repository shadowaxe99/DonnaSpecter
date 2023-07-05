```python
import os
from twilio.rest import Client

# Twilio setup
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def make_call(to_number, message):
    call = client.calls.create(
        twiml='<Response><Say>' + message + '</Say></Response>',
        from_=TWILIO_PHONE_NUMBER,
        to=to_number
    )
    return call.sid

def receive_call():
    # This function needs to be implemented based on the specific requirements
    pass

def record_call(call_sid):
    recording = client.calls(call_sid).recordings.create()
    return recording.sid
```