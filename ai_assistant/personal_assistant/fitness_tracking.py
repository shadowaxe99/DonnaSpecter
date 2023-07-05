```python
import datetime
from schemas import TaskSchema

class FitnessTracking:
    def __init__(self, user_profile, app_settings):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.fitness_data = []

    def add_fitness_activity(self, activity_type, duration, calories_burned):
        activity = {
            "type": activity_type,
            "duration": duration,
            "calories_burned": calories_burned,
            "date": datetime.datetime.now()
        }
        self.fitness_data.append(activity)
        self.updateUserProfile()

    def get_fitness_data(self):
        return self.fitness_data

    def updateUserProfile(self):
        self.user_profile['fitness_data'] = self.fitness_data
        # Trigger USER_UPDATE event
        # This is a placeholder, replace with actual event trigger
        print("USER_UPDATE")

if __name__ == "__main__":
    user_profile = {}  # This would be fetched from a database in a real application
    app_settings = {}  # This would be fetched from a database in a real application
    fitness_tracking = FitnessTracking(user_profile, app_settings)
    fitness_tracking.add_fitness_activity("Running", 30, 200)
    print(fitness_tracking.get_fitness_data())
```