```python
import os
from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def make_call(to_number, from_number=TWILIO_PHONE_NUMBER):
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        url="http://demo.twilio.com/docs/voice.xml"
    )
    return call.sid

def receive_call(call_sid):
    call = client.calls(call_sid).fetch()
    return call.to, call.from_, call.status

def record_call(call_sid):
    recording = client.calls(call_sid).recordings.create()
    return recording.sid
```