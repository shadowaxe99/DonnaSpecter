```python
import email
from email import policy
from email.parser import BytesParser

# Shared variables
USER_EMAIL = "user@example.com"
USER_CREDENTIALS = "user_credentials"

def handleEmail(raw_email):
    # Parse raw email into a message object
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)

    # Extract email subject
    subject = msg['Subject']

    # Extract email body
    if msg.is_multipart():
        for part in msg.iter_parts():
            if part.get_content_type() == 'text/plain':
                body = part.get_content()
    else:
        body = msg.get_content()

    # Extract sender's email
    from_email = email.utils.parseaddr(msg['From'])[1]

    # If the email is from the user, handle it
    if from_email == USER_EMAIL:
        processUserEmail(subject, body)

def processUserEmail(subject, body):
    # TODO: Implement user email processing logic
    pass
```