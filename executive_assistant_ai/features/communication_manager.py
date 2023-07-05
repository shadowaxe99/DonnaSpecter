```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from executive_assistant_ai.utils.logger import Logger
from executive_assistant_ai.utils.error_handler import ErrorHandler

class CommunicationManager:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.logger = Logger(__name__)
        self.error_handler = ErrorHandler(__name__)

    def send_email(self, to_email, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, to_email, text)
            server.quit()

            self.logger.log(f"Email sent to {to_email}")
        except Exception as e:
            self.error_handler.handle_error(e, "Error in sending email")

    def receive_email(self):
        # This function will be implemented in the future
        pass
```