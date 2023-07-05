```python
import twilio
from twilio.rest import Client
from ai_assistant.shared_dependencies import api_keys, user_profile

class AutomatedCalls:
    def __init__(self):
        self.client = Client(api_keys['twilio_sid'], api_keys['twilio_auth_token'])

    def make_call(self, to_number, from_number=user_profile['phone_number'], message="Hello, this is your AI assistant."):
        call = self.client.calls.create(
            twiml='<Response><Say>' + message + '</Say></Response>',
            to=to_number,
            from_=from_number
        )
        return call.sid

    def get_call_details(self, call_sid):
        call = self.client.calls.get(call_sid)
        return call

    def get_all_calls(self):
        calls = self.client.calls.list()
        return calls

automated_calls = AutomatedCalls()
```
