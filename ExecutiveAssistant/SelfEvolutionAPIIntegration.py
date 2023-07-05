```python
import requests
import json

class SelfEvolutionAPIIntegration:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.selfevolution.com"

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_tasks(self):
        response = requests.get(f"{self.base_url}/tasks", headers=self.get_headers())
        return response.json()

    def create_task(self, task_data):
        response = requests.post(f"{self.base_url}/tasks", headers=self.get_headers(), data=json.dumps(task_data))
        return response.json()

    def update_task(self, task_id, task_data):
        response = requests.put(f"{self.base_url}/tasks/{task_id}", headers=self.get_headers(), data=json.dumps(task_data))
        return response.json()

    def delete_task(self, task_id):
        response = requests.delete(f"{self.base_url}/tasks/{task_id}", headers=self.get_headers())
        return response.status_code == 204

    def get_projects(self):
        response = requests.get(f"{self.base_url}/projects", headers=self.get_headers())
        return response.json()

    def create_project(self, project_data):
        response = requests.post(f"{self.base_url}/projects", headers=self.get_headers(), data=json.dumps(project_data))
        return response.json()

    def update_project(self, project_id, project_data):
        response = requests.put(f"{self.base_url}/projects/{project_id}", headers=self.get_headers(), data=json.dumps(project_data))
        return response.json()

    def delete_project(self, project_id):
        response = requests.delete(f"{self.base_url}/projects/{project_id}", headers=self.get_headers())
        return response.status_code == 204
```