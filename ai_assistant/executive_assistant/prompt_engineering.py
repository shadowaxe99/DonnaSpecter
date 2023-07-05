```python
import json
from ai_assistant.shared_dependencies import user_profile, app_settings, api_keys
from ai_assistant.shared_dependencies import UserSchema, TaskSchema, ContactSchema
from ai_assistant.shared_dependencies import updateUserProfile, updateTask, updateContact

class PromptEngineering:
    def __init__(self):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def generate_prompt(self, task):
        """
        Generate a prompt based on the task details
        """
        task_schema = TaskSchema()
        task_details = task_schema.load(task)

        prompt = f"Dear {self.user_profile['name']}, you have a task titled {task_details['title']} due on {task_details['due_date']}."
        return prompt

    def send_prompt(self, prompt, contact):
        """
        Send the generated prompt to the specified contact
        """
        contact_schema = ContactSchema()
        contact_details = contact_schema.load(contact)

        # Use the appropriate API to send the prompt
        if contact_details['type'] == 'email':
            self.send_email_prompt(prompt, contact_details)
        elif contact_details['type'] == 'sms':
            self.send_sms_prompt(prompt, contact_details)

    def send_email_prompt(self, prompt, contact_details):
        """
        Send the prompt via email
        """
        # Use the email API to send the prompt
        # This is a placeholder and should be replaced with actual email sending code
        print(f"Sending email to {contact_details['email']} with prompt: {prompt}")

    def send_sms_prompt(self, prompt, contact_details):
        """
        Send the prompt via SMS
        """
        # Use the SMS API to send the prompt
        # This is a placeholder and should be replaced with actual SMS sending code
        print(f"Sending SMS to {contact_details['phone']} with prompt: {prompt}")

prompt_engineering = PromptEngineering()
task = json.loads('{"title": "Finish report", "due_date": "2022-12-31"}')
prompt = prompt_engineering.generate_prompt(task)
contact = json.loads('{"type": "email", "email": "user@example.com"}')
prompt_engineering.send_prompt(prompt, contact)
```