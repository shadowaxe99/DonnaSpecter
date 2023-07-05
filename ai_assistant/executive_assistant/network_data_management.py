```python
import requests
from schemas import UserSchema, TaskSchema, ContactSchema

class NetworkDataManagement:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def fetch_data(self, url):
        response = requests.get(url)
        return response.json()

    def update_user_profile(self, data):
        user_schema = UserSchema()
        validated_data = user_schema.load(data)
        self.user_profile.update(validated_data)
        return self.user_profile

    def update_task(self, data):
        task_schema = TaskSchema()
        validated_data = task_schema.load(data)
        self.app_settings['tasks'].append(validated_data)
        return self.app_settings['tasks']

    def update_contact(self, data):
        contact_schema = ContactSchema()
        validated_data = contact_schema.load(data)
        self.app_settings['contacts'].append(validated_data)
        return self.app_settings['contacts']

    def sync_data(self):
        # Sync user profile
        user_profile_url = f"https://api.example.com/user/{self.user_profile['id']}"
        user_profile_data = self.fetch_data(user_profile_url)
        self.update_user_profile(user_profile_data)

        # Sync tasks
        tasks_url = f"https://api.example.com/tasks/{self.user_profile['id']}"
        tasks_data = self.fetch_data(tasks_url)
        for task in tasks_data:
            self.update_task(task)

        # Sync contacts
        contacts_url = f"https://api.example.com/contacts/{self.user_profile['id']}"
        contacts_data = self.fetch_data(contacts_url)
        for contact in contacts_data:
            self.update_contact(contact)
```