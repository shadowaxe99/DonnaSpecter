```python
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

class HealthWellnessReminders:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()

    def add_reminder(self, reminder_time, reminder_message):
        reminder_time = datetime.datetime.strptime(reminder_time, '%H:%M').time()
        self.scheduler.add_job(self.send_reminder, 'cron', hour=reminder_time.hour, minute=reminder_time.minute, args=[reminder_message])

    def send_reminder(self, reminder_message):
        # This function will send the reminder to the user.
        # The actual implementation of this function will depend on how the user wants to receive the reminder.
        # For example, it could send an SMS using Twilio, or a Discord message, or an email, etc.
        print(reminder_message)

# Example usage:
reminders = HealthWellnessReminders()
reminders.start()
reminders.add_reminder('08:00', 'Time to drink water')
reminders.add_reminder('12:00', 'Time for a walk')
reminders.add_reminder('20:00', 'Time to prepare for sleep')
```