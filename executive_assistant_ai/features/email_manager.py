```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from executive_assistant_ai.utils.data_validator import validate_email
from executive_assistant_ai.utils.error_handler import handle_error

class EmailManager:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)

    def setup(self):
        self.server.starttls()
        self.server.login(self.email, self.password)

    def send_email(self, to_email, subject, message):
        if not validate_email(to_email):
            handle_error("Invalid email address")
            return

        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        self.server.send_message(msg)
        del msg

    def close(self):
        self.server.quit()
```