```python
import datetime
from schemas import TaskSchema

class PetCare:
    def __init__(self, user_profile, app_settings):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.pet_tasks = []

    def add_pet_task(self, task):
        new_task = TaskSchema().load(task)
        self.pet_tasks.append(new_task)
        self.updateTask(new_task)

    def remove_pet_task(self, task_id):
        for task in self.pet_tasks:
            if task['id'] == task_id:
                self.pet_tasks.remove(task)
                self.updateTask(task)
                break

    def get_pet_tasks(self):
        return self.pet_tasks

    def updateTask(self, task):
        # This function will send a TASK_UPDATE message with the updated task
        pass

    def schedule_pet_care(self, pet_name, task_name, date_time):
        task = {
            'id': len(self.pet_tasks) + 1,
            'name': task_name,
            'description': f'{task_name} for {pet_name}',
            'due_date': date_time,
            'status': 'Pending'
        }
        self.add_pet_task(task)

    def check_pet_tasks(self):
        current_time = datetime.datetime.now()
        for task in self.pet_tasks:
            if task['due_date'] <= current_time and task['status'] == 'Pending':
                print(f"Task {task['name']} for pet is due!")
                self.updateTask(task)

if __name__ == "__main__":
    pet_care = PetCare(user_profile, app_settings)
    pet_care.schedule_pet_care('Buddy', 'Vet Visit', datetime.datetime(2022, 12, 1, 10, 0))
    pet_care.check_pet_tasks()
```