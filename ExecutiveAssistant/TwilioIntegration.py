```python
from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

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