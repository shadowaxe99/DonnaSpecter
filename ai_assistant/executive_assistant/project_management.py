```python
import datetime
from typing import List
from ai_assistant.shared_dependencies import TaskSchema, updateTask

class Project:
    def __init__(self, name: str, description: str, due_date: datetime.datetime):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task: TaskSchema):
        self.tasks.append(task)
        updateTask(task)

class ProjectManagement:
    def __init__(self):
        self.projects = []

    def create_project(self, name: str, description: str, due_date: datetime.datetime):
        project = Project(name, description, due_date)
        self.projects.append(project)
        return project

    def get_project(self, name: str):
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def delete_project(self, name: str):
        self.projects = [project for project in self.projects if project.name != name]

    def add_task_to_project(self, project_name: str, task: TaskSchema):
        project = self.get_project(project_name)
        if project:
            project.add_task(task)
        else:
            raise Exception(f"Project {project_name} not found")

    def get_all_tasks(self, project_name: str) -> List[TaskSchema]:
        project = self.get_project(project_name)
        if project:
            return project.tasks
        else:
            raise Exception(f"Project {project_name} not found")
```