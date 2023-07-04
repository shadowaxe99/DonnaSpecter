```python
from flask import Flask, request, jsonify
from src.ai_model import gpt4
from src.email_handler import mime_handler
from src.scheduler import google_calendar, microsoft_graph

app = Flask(__name__)

@app.route('/api/v1/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    user_email = data.get('USER_EMAIL')
    query = data.get('query')

    # Process the query with GPT-4 model
    response = gpt4.process_query(query)

    # Handle email related tasks
    if 'email' in response:
        mime_handler.handleEmail(user_email, response['email'])

    # Handle scheduling tasks
    if 'task' in response:
        if response['platform'] == 'google':
            google_calendar.scheduleTask(user_email, response['task'])
        elif response['platform'] == 'microsoft':
            microsoft_graph.scheduleTask(user_email, response['task'])

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```