```python
import requests
from schemas import UserSchema, ContactSchema

class CustomerSupport:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def create_ticket(self, issue_description, priority):
        ticket_data = {
            "user": self.user_profile,
            "issue_description": issue_description,
            "priority": priority
        }
        response = requests.post(self.app_settings['customer_support_url'], data=ticket_data, headers=self.api_keys)
        return response.json()

    def update_ticket(self, ticket_id, status):
        ticket_data = {
            "status": status
        }
        response = requests.put(f"{self.app_settings['customer_support_url']}/{ticket_id}", data=ticket_data, headers=self.api_keys)
        return response.json()

    def get_ticket(self, ticket_id):
        response = requests.get(f"{self.app_settings['customer_support_url']}/{ticket_id}", headers=self.api_keys)
        return response.json()

    def delete_ticket(self, ticket_id):
        response = requests.delete(f"{self.app_settings['customer_support_url']}/{ticket_id}", headers=self.api_keys)
        return response.json()

def updateUserProfile(user_profile):
    cs = CustomerSupport(user_profile, app_settings, api_keys)
    return cs

def updateContact(contact):
    cs = CustomerSupport(user_profile, app_settings, api_keys)
    return cs
```