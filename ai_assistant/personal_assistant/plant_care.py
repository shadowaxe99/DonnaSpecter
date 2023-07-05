```python
import datetime
from ai_assistant.shared_dependencies import user_profile, TaskSchema, updateTask

class PlantCare:
    def __init__(self):
        self.plants = user_profile.get('plants', [])

    def add_plant(self, plant_name, watering_frequency):
        new_plant = {
            'name': plant_name,
            'watering_frequency': watering_frequency,
            'last_watered': None
        }
        self.plants.append(new_plant)
        user_profile['plants'] = self.plants

    def water_plant(self, plant_name):
        for plant in self.plants:
            if plant['name'] == plant_name:
                plant['last_watered'] = datetime.datetime.now()
                user_profile['plants'] = self.plants
                return f"{plant_name} has been watered."

        return f"No plant named {plant_name} found."

    def check_watering(self):
        tasks = []
        for plant in self.plants:
            if plant['last_watered'] is None or (datetime.datetime.now() - plant['last_watered']).days >= plant['watering_frequency']:
                task = TaskSchema(name=f"Water {plant['name']}", category="Plant Care")
                tasks.append(task)
        for task in tasks:
            updateTask(task)
        return tasks

plant_care = PlantCare()
```