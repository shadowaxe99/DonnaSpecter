```python
import datetime
from ai_assistant.scheduler import schedule
from ai_assistant.email_notifications import emailNotification

class TaskAutomation:
    def __init__(self, user_profile, task_list):
        self.user_profile = user_profile
        self.task_list = task_list

    def automateTask(self, task):
        if task['due_date'] < datetime.datetime.now():
            return "Task is already overdue!"
        else:
            schedule(task['due_date'], task['task_id'])
            emailNotification(self.user_profile['email'], "New task scheduled: " + task['task_name'])
            return "Task scheduled successfully!"

    def checkTasks(self):
        for task in self.task_list:
            if task['due_date'] < datetime.datetime.now():
                emailNotification(self.user_profile['email'], "Task is overdue: " + task['task_name'])
            elif task['due_date'] - datetime.datetime.now() < datetime.timedelta(days=1):
                emailNotification(self.user_profile['email'], "Task is due soon: " + task['task_name'])

    def updateTask(self, task_id, new_task):
        for task in self.task_list:
            if task['task_id'] == task_id:
                task = new_task
                emailNotification(self.user_profile['email'], "Task updated: " + task['task_name'])
                return "Task updated successfully!"
        return "Task not found!"

    def deleteTask(self, task_id):
        for task in self.task_list:
            if task['task_id'] == task_id:
                self.task_list.remove(task)
                emailNotification(self.user_profile['email'], "Task deleted: " + task['task_name'])
                return "Task deleted successfully!"
        return "Task not found!"
```