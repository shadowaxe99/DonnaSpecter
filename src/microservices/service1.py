```python
from flask import Flask, request
from src.ai_model.gpt4 import process_query
from src.email_handler.mime_handler import handle_email
from src.scheduler.google_calendar import schedule_task
from src.security.oauth2 import authenticate_user
from src.database.postgresql import connect_db

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_user_query():
    data = request.get_json()
    user_email = data.get('USER_EMAIL')
    user_credentials = data.get('USER_CREDENTIALS')
    query = data.get('query')

    # Authenticate user
    user = authenticate_user(user_email, user_credentials)
    if not user:
        return {'error': 'Invalid credentials'}, 401

    # Process the query using GPT-4 model
    response = process_query(query)

    return {'response': response}, 200

@app.route('/handle_email', methods=['POST'])
def process_email():
    data = request.get_json()
    user_email = data.get('USER_EMAIL')
    email_data = data.get('email_data')

    # Handle the email
    handle_email(user_email, email_data)

    return {'status': 'Email processed successfully'}, 200

@app.route('/schedule_task', methods=['POST'])
def schedule_user_task():
    data = request.get_json()
    user_email = data.get('USER_EMAIL')
    task_data = data.get('task_data')

    # Schedule the task
    schedule_task(user_email, task_data)

    return {'status': 'Task scheduled successfully'}, 200

if __name__ == '__main__':
    # Connect to the database
    connect_db()
    app.run(host='0.0.0.0', port=5000)
```