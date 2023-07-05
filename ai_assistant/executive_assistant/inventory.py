```python
import json
from schemas import TaskSchema

class Inventory:
    def __init__(self, user_profile, app_settings):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.inventory = self.load_inventory()

    def load_inventory(self):
        try:
            with open('inventory.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.inventory, file)

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory[item] = 1
        else:
            self.inventory[item] += 1
        self.save_inventory()

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                del self.inventory[item]
            self.save_inventory()

    def get_inventory(self):
        return self.inventory

    def update_user_profile(self):
        self.user_profile['inventory'] = self.get_inventory()
        updateUserProfile(self.user_profile)

    def update_task(self, task):
        task_schema = TaskSchema()
        if task_schema.validate(task):
            updateTask(task)
        else:
            raise ValueError("Invalid task data")

    def update_contact(self, contact):
        contact_schema = ContactSchema()
        if contact_schema.validate(contact):
            updateContact(contact)
        else:
            raise ValueError("Invalid contact data")
```