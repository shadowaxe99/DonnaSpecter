```python
import datetime
from ai_assistant.zoom_invites import zoomInvite
from ai_assistant.google_meets import googleMeet
from ai_assistant.email_notifications import emailNotification

class Scheduler:
    def __init__(self, user_profile, meeting_data):
        self.user_profile = user_profile
        self.meeting_data = meeting_data

    def schedule(self):
        for meeting in self.meeting_data:
            if meeting['platform'] == 'zoom':
                zoomInvite(self.user_profile, meeting)
            elif meeting['platform'] == 'google_meet':
                googleMeet(self.user_profile, meeting)
            emailNotification(self.user_profile, meeting)

    def checkAvailability(self, start_time, end_time):
        start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        for meeting in self.meeting_data:
            meeting_start = datetime.datetime.strptime(meeting['start_time'], '%Y-%m-%d %H:%M:%S')
            meeting_end = datetime.datetime.strptime(meeting['end_time'], '%Y-%m-%d %H:%M:%S')
            if start <= meeting_end and meeting_start <= end:
                return False
        return True
```