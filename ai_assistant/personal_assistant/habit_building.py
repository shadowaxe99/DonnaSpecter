```python
import datetime
from ai_assistant.shared_dependencies import TaskSchema, updateTask, user_profile

class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
        self.last_completed = None

    def complete_habit(self):
        self.last_completed = datetime.datetime.now()
        self.update_user_profile()

    def update_user_profile(self):
        user_profile['habits'][self.name] = self.last_completed
        updateTask('Habit Update', f'Habit {self.name} was completed.')

class HabitBuilder:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name, frequency):
        self.habits[name] = Habit(name, frequency)

    def complete_habit(self, name):
        if name in self.habits:
            self.habits[name].complete_habit()
        else:
            print(f'Habit {name} does not exist.')

    def view_habits(self):
        for habit in self.habits.values():
            print(f'Habit: {habit.name}, Frequency: {habit.frequency}, Last Completed: {habit.last_completed}')

habit_builder = HabitBuilder()
```