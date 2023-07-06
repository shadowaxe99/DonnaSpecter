import os
from dotenv import load_dotenv
from productivity_tools import Todoist, Trello, Asana

load_dotenv()

TODOIST_API_KEY = os.getenv('TODOIST_API_KEY')
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
ASANA_TOKEN = os.getenv('ASANA_TOKEN')

todoist = Todoist(TODOIST_API_KEY)
trello = Trello(TRELLO_API_KEY, TRELLO_TOKEN)
asana = Asana(ASANA_TOKEN)

def integrateProductivityTool(user_profile, task_list):
    if user_profile['productivity_tool'] == 'Todoist':
        for task in task_list:
            todoist.create_task(task['title'], task['due_date'])
    elif user_profile['productivity_tool'] == 'Trello':
        for task in task_list:
            trello.create_card(task['title'], task['due_date'])
    elif user_profile['productivity_tool'] == 'Asana':
        for task in task_list:
            asana.create_task(task['title'], task['due_date'])
    else:
        print("Unsupported productivity tool.")