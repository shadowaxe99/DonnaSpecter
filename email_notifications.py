import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ai_assistant.scheduler import schedule
from ai_assistant.user_profile import UserProfileSchema

def emailNotification(user_profile: UserProfileSchema, meeting_data: dict):
    # create message object instance
    msg = MIMEMultipart()

    message = f"Dear {user_profile.name},\n\nYou have a meeting scheduled at {meeting_data['time']}. The meeting details are as follows:\n\n{meeting_data['details']}"

    # setup the parameters of the message
    password = "YOUR_PASSWORD"
    msg['From'] = "YOUR_EMAIL"
    msg['To'] = user_profile.email
    msg['Subject'] = "Meeting Notification"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print(f"successfully sent email to {msg['To']}")

def notifyAllUsers():
    for user in UserProfileSchema.query.all():
        schedule_data = schedule(user)
        emailNotification(user, schedule_data)
