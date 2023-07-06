import pandas as pd
from datetime import datetime
from ai_assistant.shared_dependencies import meeting_data

class MeetingAnalytics:
    def __init__(self):
        self.meeting_data = meeting_data

    def get_meeting_duration(self, meeting_id):
        meeting = self.meeting_data[meeting_id]
        start_time = datetime.strptime(meeting['start_time'], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(meeting['end_time'], '%Y-%m-%d %H:%M:%S')
        duration = end_time - start_time
        return duration.total_seconds() / 60

    def get_average_meeting_duration(self):
        total_duration = 0
        for meeting_id in self.meeting_data:
            total_duration += self.get_meeting_duration(meeting_id)
        return total_duration / len(self.meeting_data)

    def get_participant_count(self, meeting_id):
        meeting = self.meeting_data[meeting_id]
        return len(meeting['participants'])

    def get_average_participant_count(self):
        total_participants = 0
        for meeting_id in self.meeting_data:
            total_participants += self.get_participant_count(meeting_id)
        return total_participants / len(self.meeting_data)

    def get_meeting_frequency(self):
        dates = [datetime.strptime(meeting['start_time'], '%Y-%m-%d %H:%M:%S').date() for meeting in self.meeting_data.values()]
        date_counts = pd.Series(dates).value_counts().sort_index()
        return date_counts.to_dict()

    def analyze_meeting(self):
        average_duration = self.get_average_meeting_duration()
        average_participants = self.get_average_participant_count()
        meeting_frequency = self.get_meeting_frequency()
        return {
            'average_duration': average_duration,
            'average_participants': average_participants,
            'meeting_frequency': meeting_frequency
        }