```python
import datetime

class Project:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_project_duration(self):
        return self.end_date - self.start_date

    def get_tasks(self):
        return self.tasks


class Task:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Not Started"

    def start_task(self):
        self.status = "In Progress"

    def complete_task(self):
        self.status = "Completed"

    def get_task_duration(self):
        return self.end_date - self.start_date

    def get_status(self):
        return self.status


class ProjectManagement:
    def __init__(self):
        self.projects = []

    def create_project(self, name, description, start_date, end_date):
        project = Project(name, description, start_date, end_date)
        self.projects.append(project)
        return project

    def remove_project(self, project):
        self.projects.remove(project)

    def get_projects(self):
        return self.projects
```