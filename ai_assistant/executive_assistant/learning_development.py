```python
import requests
from schemas import UserSchema

class LearningDevelopment:
    def __init__(self, user_profile, app_settings):
        self.user_profile = user_profile
        self.app_settings = app_settings

    def fetch_courses(self):
        # Fetch courses based on user's interests and learning goals
        interests = self.user_profile.get('interests', [])
        learning_goals = self.user_profile.get('learning_goals', [])

        # API call to fetch courses
        response = requests.get(self.app_settings['learning_api_url'], params={'interests': interests, 'goals': learning_goals})

        if response.status_code == 200:
            return response.json()
        else:
            return []

    def recommend_courses(self):
        # Fetch courses
        courses = self.fetch_courses()

        # Recommend top 5 courses based on user's learning style
        learning_style = self.user_profile.get('learning_style', 'Visual')
        recommended_courses = [course for course in courses if course['learning_style'] == learning_style][:5]

        return recommended_courses

    def update_learning_goals(self, new_goals):
        # Update user's learning goals
        self.user_profile['learning_goals'] = new_goals
        UserSchema().load(self.user_profile)

        # Trigger USER_UPDATE message
        requests.post(self.app_settings['message_api_url'], data={'message_name': 'USER_UPDATE', 'data': self.user_profile})

    def update_learning_style(self, new_style):
        # Update user's learning style
        self.user_profile['learning_style'] = new_style
        UserSchema().load(self.user_profile)

        # Trigger USER_UPDATE message
        requests.post(self.app_settings['message_api_url'], data={'message_name': 'USER_UPDATE', 'data': self.user_profile})
```