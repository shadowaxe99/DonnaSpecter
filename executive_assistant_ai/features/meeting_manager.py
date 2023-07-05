```python
import datetime
from executive_assistant_ai.utils.data_validator import validate_meeting_data
from executive_assistant_ai.utils.error_handler import handle_error
from executive_assistant_ai.utils.logger import log

class MeetingManager:
    def __init__(self):
        self.meetings = []

    def schedule_meeting(self, meeting_data):
        try:
            if validate_meeting_data(meeting_data):
                self.meetings.append(meeting_data)
                log("Meeting scheduled successfully.")
            else:
                handle_error("Invalid meeting data.")
        except Exception as e:
            handle_error(str(e))

    def cancel_meeting(self, meeting_id):
        try:
            self.meetings = [meeting for meeting in self.meetings if meeting['id'] != meeting_id]
            log("Meeting cancelled successfully.")
        except Exception as e:
            handle_error(str(e))

    def reschedule_meeting(self, meeting_id, new_time):
        try:
            for meeting in self.meetings:
                if meeting['id'] == meeting_id:
                    meeting['time'] = new_time
                    log("Meeting rescheduled successfully.")
                    break
            else:
                handle_error("Meeting not found.")
        except Exception as e:
            handle_error(str(e))

    def get_upcoming_meetings(self):
        try:
            upcoming_meetings = [meeting for meeting in self.meetings if meeting['time'] > datetime.datetime.now()]
            return upcoming_meetings
        except Exception as e:
            handle_error(str(e))

    def get_past_meetings(self):
        try:
            past_meetings = [meeting for meeting in self.meetings if meeting['time'] < datetime.datetime.now()]
            return past_meetings
        except Exception as e:
            handle_error(str(e))
```