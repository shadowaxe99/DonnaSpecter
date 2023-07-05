```python
import os
from getpass import getpass

def initiateOnboarding():
    print("Welcome to the AI Executive Assistant and Personal Assistant onboarding process!")

    # User Profile Setup
    user_profile = {}
    user_profile['name'] = input("Please enter your name: ")
    user_profile['email'] = input("Please enter your email: ")
    user_profile['password'] = getpass("Please enter your password: ")

    # App Settings Setup
    app_settings = {}
    app_settings['theme'] = input("Please choose a theme (light/dark): ")
    app_settings['notifications'] = input("Enable notifications? (yes/no): ")

    # API Keys Setup
    api_keys = {}
    api_keys['google'] = getpass("Please enter your Google API key: ")
    api_keys['twilio'] = getpass("Please enter your Twilio API key: ")
    api_keys['eleven_labs'] = getpass("Please enter your Eleven Labs API key: ")

    # Save user_profile, app_settings, and api_keys to a file
    with open(os.path.join(os.path.dirname(__file__), '../user_data/user_profile.py'), 'w') as file:
        file.write(str(user_profile))

    with open(os.path.join(os.path.dirname(__file__), '../user_data/app_settings.py'), 'w') as file:
        file.write(str(app_settings))

    with open(os.path.join(os.path.dirname(__file__), '../user_data/api_keys.py'), 'w') as file:
        file.write(str(api_keys))

    print("Onboarding process completed successfully!")

if __name__ == "__main__":
    initiateOnboarding()
```