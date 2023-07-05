```python
import re

class DataCleaner:
    def __init__(self):
        pass

    def clean_user_data(self, user_data):
        cleaned_data = {}
        for key, value in user_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_schedule_data(self, schedule_data):
        cleaned_data = {}
        for key, value in schedule_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_email_data(self, email_data):
        cleaned_data = {}
        for key, value in email_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_meeting_data(self, meeting_data):
        cleaned_data = {}
        for key, value in meeting_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_task_data(self, task_data):
        cleaned_data = {}
        for key, value in task_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_reminder_data(self, reminder_data):
        cleaned_data = {}
        for key, value in reminder_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_note_data(self, note_data):
        cleaned_data = {}
        for key, value in note_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_communication_data(self, communication_data):
        cleaned_data = {}
        for key, value in communication_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_report_data(self, report_data):
        cleaned_data = {}
        for key, value in report_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_expense_data(self, expense_data):
        cleaned_data = {}
        for key, value in expense_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_travel_data(self, travel_data):
        cleaned_data = {}
        for key, value in travel_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def clean_time_data(self, time_data):
        cleaned_data = {}
        for key, value in time_data.items():
            cleaned_data[key] = self._clean_string(value)
        return cleaned_data

    def _clean_string(self, string):
        string = re.sub(r'\s+', ' ', string)  # remove extra spaces
        string = string.strip()  # remove leading and trailing spaces
        return string
```