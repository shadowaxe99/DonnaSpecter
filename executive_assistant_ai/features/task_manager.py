```python
import datetime
from executive_assistant_ai.utils.data_validator import validate_task
from executive_assistant_ai.utils.error_handler import handle_error
from executive_assistant_ai.utils.logger import log

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        try:
            validate_task(task)
            self.tasks.append(task)
            log(f"Task added: {task}")
        except Exception as e:
            handle_error(e)

    def remove_task(self, task_id):
        try:
            task_to_remove = next(task for task in self.tasks if task['id'] == task_id)
            self.tasks.remove(task_to_remove)
            log(f"Task removed: {task_to_remove}")
        except Exception as e:
            handle_error(e)

    def update_task(self, task_id, updated_task):
        try:
            validate_task(updated_task)
            task_to_update = next(task for task in self.tasks if task['id'] == task_id)
            task_to_update.update(updated_task)
            log(f"Task updated: {task_to_update}")
        except Exception as e:
            handle_error(e)

    def get_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id):
        try:
            task = next(task for task in self.tasks if task['id'] == task_id)
            return task
        except Exception as e:
            handle_error(e)

    def get_tasks_by_date(self, date):
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object")
        tasks_on_date = [task for task in self.tasks if task['date'] == date]
        return tasks_on_date
```