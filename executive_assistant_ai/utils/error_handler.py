```python
import logging
from executive_assistant_ai.utils.logger import Logger

class ErrorHandler:
    def __init__(self):
        self.logger = Logger(__name__)

    def handle_error(self, error):
        self.logger.log_error(error)
        self._display_error_message(error)

    def _display_error_message(self, error):
        print(f"An error occurred: {str(error)}")

    def handle_exception(self, exception):
        self.logger.log_exception(exception)
        self._display_exception_message(exception)

    def _display_exception_message(self, exception):
        print(f"An exception occurred: {str(exception)}")
```