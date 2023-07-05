```python
import json
from schemas import UserSchema, TaskSchema

class HR:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def update_user_profile(self, new_data):
        user_schema = UserSchema()
        validated_data = user_schema.load(new_data)
        self.user_profile.update(validated_data)
        return json.dumps(self.user_profile)

    def add_task(self, task_data):
        task_schema = TaskSchema()
        validated_data = task_schema.load(task_data)
        self.app_settings['tasks'].append(validated_data)
        return json.dumps(self.app_settings['tasks'])

    def update_task(self, task_id, task_data):
        task_schema = TaskSchema()
        validated_data = task_schema.load(task_data)
        for task in self.app_settings['tasks']:
            if task['id'] == task_id:
                task.update(validated_data)
                return json.dumps(task)
        return 'Task not found'

    def delete_task(self, task_id):
        for task in self.app_settings['tasks']:
            if task['id'] == task_id:
                self.app_settings['tasks'].remove(task)
                return 'Task deleted'
        return 'Task not found'
```