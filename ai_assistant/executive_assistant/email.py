```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def send_email(self, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.user_profile['email']
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.user_profile['email'], self.api_keys['email'])
        text = msg.as_string()
        server.sendmail(self.user_profile['email'], recipient, text)
        server.quit()

    def update_contact(self, contact):
        self.user_profile['contacts'].append(contact)
        return self.user_profile

    def update_user_profile(self, user_profile):
        self.user_profile = user_profile
        return self.user_profile
```