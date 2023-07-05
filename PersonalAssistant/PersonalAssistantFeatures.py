```python
import datetime
from twilio_integration import send_message
from discord_integration import send_message as send_discord_message

class PersonalAssistantFeatures:
    def __init__(self):
        self.shopping_list = []
        self.appointments = []
        self.social_events = []

    def add_to_shopping_list(self, item):
        self.shopping_list.append(item)
        return f"{item} added to shopping list."

    def remove_from_shopping_list(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            return f"{item} removed from shopping list."
        else:
            return f"{item} not found in shopping list."

    def view_shopping_list(self):
        return self.shopping_list

    def book_appointment(self, appointment_details):
        self.appointments.append(appointment_details)
        return f"Appointment booked: {appointment_details}"

    def cancel_appointment(self, appointment_details):
        if appointment_details in self.appointments:
            self.appointments.remove(appointment_details)
            return f"Appointment cancelled: {appointment_details}"
        else:
            return f"No such appointment found: {appointment_details}"

    def view_appointments(self):
        return self.appointments

    def schedule_social_event(self, event_details):
        self.social_events.append(event_details)
        return f"Social event scheduled: {event_details}"

    def cancel_social_event(self, event_details):
        if event_details in self.social_events:
            self.social_events.remove(event_details)
            return f"Social event cancelled: {event_details}"
        else:
            return f"No such social event found: {event_details}"

    def view_social_events(self):
        return self.social_events

    def send_reminder(self, reminder_details, platform):
        if platform == "twilio":
            send_message(reminder_details)
        elif platform == "discord":
            send_discord_message(reminder_details)
        else:
            return "Invalid platform. Please choose between 'twilio' and 'discord'."

    def set_reminder(self, reminder_details, platform, time):
        current_time = datetime.datetime.now()
        difference = time - current_time
        if difference.total_seconds() > 0:
            threading.Timer(difference.total_seconds(), self.send_reminder, [reminder_details, platform]).start()
            return f"Reminder set for {time}."
        else:
            return "Invalid time. Please choose a future time."
```