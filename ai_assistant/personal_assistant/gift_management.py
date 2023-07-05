```python
import datetime
from ai_assistant.shared_dependencies import user_profile, TaskSchema, updateTask

class GiftManagement:
    def __init__(self):
        self.gifts = []

    def add_gift(self, recipient, gift, date):
        gift_task = TaskSchema({
            "task_type": "gift",
            "recipient": recipient,
            "gift": gift,
            "date": date
        })
        self.gifts.append(gift_task)
        updateTask(gift_task)

    def remove_gift(self, gift_task):
        self.gifts.remove(gift_task)
        updateTask(gift_task)

    def get_upcoming_gifts(self):
        today = datetime.date.today()
        upcoming_gifts = [gift for gift in self.gifts if gift["date"] > today]
        return upcoming_gifts

    def get_gifts_for_recipient(self, recipient):
        recipient_gifts = [gift for gift in self.gifts if gift["recipient"] == recipient]
        return recipient_gifts

gift_management = GiftManagement()

def handle_new_user():
    user_gifts = user_profile.get("gifts", [])
    for gift in user_gifts:
        gift_management.add_gift(gift["recipient"], gift["gift"], gift["date"])

handle_new_user()
```