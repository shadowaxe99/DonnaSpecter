```python
import os
from flask import Flask, request
from src.ai_model.gpt4 import process_query
from src.scheduler.google_calendar import schedule_task
from src.security.oauth2 import authenticate_user

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def handle_query():
    data = request.get_json()
    user_email = data.get('user_email')
    query = data.get('query')

    # Authenticate user
    user_credentials = authenticate_user(user_email)
    if not user_credentials:
        return {'error': 'Invalid user credentials'}, 401

    # Process query using GPT-4 model
    task = process_query(query)
    if not task:
        return {'error': 'Unable to process query'}, 400

    # Schedule task
    task_status = schedule_task(user_email, user_credentials, task)
    if not task_status:
        return {'error': 'Unable to schedule task'}, 500

    return {'message': 'Task scheduled successfully'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```