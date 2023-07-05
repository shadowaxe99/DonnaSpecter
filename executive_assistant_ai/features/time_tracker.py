```python
import datetime
from executive_assistant_ai.utils import data_validator
from executive_assistant_ai.utils import error_handler
from executive_assistant_ai.utils import logger

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total_time = None

    def start_tracking(self):
        self.start_time = datetime.datetime.now()
        logger.log("Time tracking started at {}".format(self.start_time))

    def stop_tracking(self):
        if self.start_time is None:
            error_handler.handle_error("Time tracking has not been started yet.")
            return

        self.end_time = datetime.datetime.now()
        self.total_time = self.end_time - self.start_time
        logger.log("Time tracking stopped at {}. Total time: {}".format(self.end_time, self.total_time))

    def get_total_time(self):
        if self.total_time is None:
            error_handler.handle_error("Time tracking has not been started or stopped yet.")
            return

        return self.total_time

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.total_time = None
        logger.log("Time tracking reset.")

    def validate_time(self, time):
        if not data_validator.validate_time(time):
            error_handler.handle_error("Invalid time format.")
            return False

        return True
```