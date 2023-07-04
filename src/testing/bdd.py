```python
from behave import given, when, then
from src.ai_model.gpt4 import GPT4Model
from src.email_handler.mime_handler import MimeHandler
from src.scheduler.google_calendar import GoogleCalendar
from src.scheduler.microsoft_graph import MicrosoftGraph
from src.security.oauth2 import OAuth2
from src.database.postgresql import PostgreSQL
from src.database.mongodb import MongoDB

@given('the AI model is initialized')
def step_given_ai_model_is_initialized(context):
    context.ai_model = GPT4Model()

@given('the email handler is initialized')
def step_given_email_handler_is_initialized(context):
    context.email_handler = MimeHandler()

@given('the Google Calendar scheduler is initialized')
def step_given_google_calendar_scheduler_is_initialized(context):
    context.google_calendar = GoogleCalendar()

@given('the Microsoft Graph scheduler is initialized')
def step_given_microsoft_graph_scheduler_is_initialized(context):
    context.microsoft_graph = MicrosoftGraph()

@given('the OAuth2 security is initialized')
def step_given_oauth2_security_is_initialized(context):
    context.oauth2 = OAuth2()

@given('the PostgreSQL database is initialized')
def step_given_postgresql_database_is_initialized(context):
    context.postgresql = PostgreSQL()

@given('the MongoDB database is initialized')
def step_given_mongodb_database_is_initialized(context):
    context.mongodb = MongoDB()

@when('the user sends an email')
def step_when_user_sends_an_email(context):
    context.email_handler.handleEmail()

@when('the user schedules a task')
def step_when_user_schedules_a_task(context):
    context.ai_model.scheduleTask()

@then('the email should be processed')
def step_then_email_should_be_processed(context):
    assert context.email_handler.processed

@then('the task should be scheduled')
def step_then_task_should_be_scheduled(context):
    assert context.ai_model.scheduled

@then('the user data should be secure')
def step_then_user_data_should_be_secure(context):
    assert context.oauth2.secure

@then('the database should be updated')
def step_then_database_should_be_updated(context):
    assert context.postgresql.updated or context.mongodb.updated
```