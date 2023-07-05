```python
from twilio.rest import Client
from ai_assistant.shared_dependencies import api_keys, user_profile

class TwilioIntegration:
    def __init__(self):
        self.client = Client(api_keys['twilio_sid'], api_keys['twilio_auth_token'])

    def send_sms(self, to, body):
        message = self.client.messages.create(
            body=body,
            from_=user_profile['twilio_phone_number'],
            to=to
        )
        return message.sid

    def make_call(self, to, url):
        call = self.client.calls.create(
            url=url,
            to=to,
            from_=user_profile['twilio_phone_number']
        )
        return call.sid

    def fetch_call(self, call_sid):
        call = self.client.calls(call_sid).fetch()
        return call

    def fetch_sms(self, message_sid):
        message = self.client.messages(message_sid).fetch()
        return message
```