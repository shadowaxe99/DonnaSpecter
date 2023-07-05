```python
import requests
import json

ELEVEN_LABS_API_KEY = 'your_api_key_here'

def get_projects():
    response = requests.get(
        'https://api.elevenlabs.com/projects',
        headers={'Authorization': 'Bearer ' + ELEVEN_LABS_API_KEY}
    )
    return response.json()

def create_project(name, description):
    data = {
        'name': name,
        'description': description
    }
    response = requests.post(
        'https://api.elevenlabs.com/projects',
        headers={'Authorization': 'Bearer ' + ELEVEN_LABS_API_KEY},
        data=json.dumps(data)
    )
    return response.json()

def update_project(project_id, name, description):
    data = {
        'name': name,
        'description': description
    }
    response = requests.put(
        f'https://api.elevenlabs.com/projects/{project_id}',
        headers={'Authorization': 'Bearer ' + ELEVEN_LABS_API_KEY},
        data=json.dumps(data)
    )
    return response.json()

def delete_project(project_id):
    response = requests.delete(
        f'https://api.elevenlabs.com/projects/{project_id}',
        headers={'Authorization': 'Bearer ' + ELEVEN_LABS_API_KEY}
    )
    return response.status_code == 204
```