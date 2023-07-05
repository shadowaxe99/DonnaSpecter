```python
import datetime
from schemas import UserSchema

class MoodTrackingSupport:
    def __init__(self, user_profile, app_settings):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.mood_data = []

    def track_mood(self, mood_score):
        """
        Track user's mood score and timestamp it.
        """
        timestamp = datetime.datetime.now()
        self.mood_data.append({"timestamp": timestamp, "mood_score": mood_score})
        self.updateUserProfile()

    def get_mood_data(self):
        """
        Return user's mood data.
        """
        return self.mood_data

    def updateUserProfile(self):
        """
        Update user profile with latest mood data.
        """
        self.user_profile['mood_data'] = self.mood_data
        UserSchema().load(self.user_profile)

    def provide_support(self, mood_score):
        """
        Provide support based on user's mood score.
        """
        if mood_score < 3:
            return "We're here for you. Don't hesitate to reach out."
        elif mood_score < 5:
            return "Keep going, things will get better."
        else:
            return "Great to see you're feeling good!"

if __name__ == "__main__":
    user_profile = {"name": "John Doe", "mood_data": []}
    app_settings = {"language": "English"}
    mood_tracker = MoodTrackingSupport(user_profile, app_settings)
    mood_tracker.track_mood(4)
    print(mood_tracker.provide_support(4))
```