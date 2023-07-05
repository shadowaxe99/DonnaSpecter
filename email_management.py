```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailManager:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def send_email(self, to_address, subject, body, attachment=None):
        msg = MIMEMultipart()
        msg['From'] = self.user_profile['email']
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment:
            attachment_file = open(attachment, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment_file).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % attachment)
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.user_profile['email'], self.user_profile['password'])
        text = msg.as_string()
        server.sendmail(self.user_profile['email'], to_address, text)
        server.quit()

    def manage_inbox(self):
        # This function can be expanded to include logic for managing the inbox
        pass

    def manage_sent(self):
        # This function can be expanded to include logic for managing sent emails
        pass

    def manage_drafts(self):
        # This function can be expanded to include logic for managing drafts
        pass
```