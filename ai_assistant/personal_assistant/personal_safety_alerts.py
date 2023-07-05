```python
import requests
from datetime import datetime

class PersonalSafetyAlerts:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def send_alert(self, message):
        # Here we assume that the user's contact information is stored in the user_profile
        contact_info = self.user_profile['contact_info']
        for contact in contact_info:
            if contact['type'] == 'email':
                self.send_email(contact['value'], message)
            elif contact['type'] == 'phone':
                self.send_sms(contact['value'], message)

    def send_email(self, email, message):
        # Here we assume that we have an SMTP server setup for sending emails
        # This is a placeholder and should be replaced with actual SMTP server details
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login("your_email", "your_password")
        server.sendmail("your_email", email, message)
        server.quit()

    def send_sms(self, phone, message):
        # Here we assume that we are using Twilio for sending SMS
        # This is a placeholder and should be replaced with actual Twilio account details
        account_sid = self.api_keys['twilio']['account_sid']
        auth_token = self.api_keys['twilio']['auth_token']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_='+12345678901',
            to=phone
        )

    def check_and_send_alerts(self):
        # Check if there are any safety alerts for the user
        # This is a placeholder and should be replaced with actual logic for checking safety alerts
        if datetime.now().hour > 22:
            self.send_alert("It's late, please be safe.")
```
