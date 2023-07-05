```python
import datetime
from executive_assistant_ai.utils import data_validator, data_cleaner, error_handler, logger

class ScheduleManager:
    def __init__(self):
        self.schedule_data = []

    def add_event(self, event):
        try:
            data_validator.validate_event_data(event)
            self.schedule_data.append(event)
            logger.log("Event added successfully.")
        except Exception as e:
            error_handler.handle_error(e)

    def remove_event(self, event_id):
        try:
            self.schedule_data = [event for event in self.schedule_data if event['id'] != event_id]
            logger.log("Event removed successfully.")
        except Exception as e:
            error_handler.handle_error(e)

    def update_event(self, event_id, updated_event):
        try:
            data_validator.validate_event_data(updated_event)
            for event in self.schedule_data:
                if event['id'] == event_id:
                    event.update(updated_event)
                    logger.log("Event updated successfully.")
                    break
        except Exception as e:
            error_handler.handle_error(e)

    def get_event(self, event_id):
        try:
            for event in self.schedule_data:
                if event['id'] == event_id:
                    return event
            logger.log("Event not found.")
        except Exception as e:
            error_handler.handle_error(e)

    def get_schedule(self, date=datetime.date.today()):
        try:
            schedule = [event for event in self.schedule_data if event['date'] == date]
            return schedule
        except Exception as e:
            error_handler.handle_error(e)

    def clean_schedule(self):
        try:
            self.schedule_data = data_cleaner.clean_data(self.schedule_data)
            logger.log("Schedule cleaned successfully.")
        except Exception as e:
            error_handler.handle_error(e)
```