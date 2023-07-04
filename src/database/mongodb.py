```python
from pymongo import MongoClient
from src.security.encryption import decryptData

# MongoDB connection string
DB_CONNECTION = decryptData("DB_CONNECTION")

# Establish a connection to the MongoDB
client = MongoClient(DB_CONNECTION)

# Select the database
db = client.ai_scheduling_assistant

# Define the User, Task and Email collections
users = db.users
tasks = db.tasks
emails = db.emails

# Define the User, Task and Email schemas
UserSchema = {
    "email": "USER_EMAIL",
    "credentials": "USER_CREDENTIALS",
    "tasks": [],
    "emails": []
}

TaskSchema = {
    "user_email": "USER_EMAIL",
    "description": "",
    "date": "",
    "status": ""
}

EmailSchema = {
    "user_email": "USER_EMAIL",
    "subject": "",
    "body": "",
    "attachments": []
}

def connectDB():
    try:
        client.server_info()  # Will throw an exception if not connected
        print("Successfully connected to MongoDB")
    except:
        print("Failed to connect to MongoDB")

def insert_user(user):
    users.insert_one(user)

def insert_task(task):
    tasks.insert_one(task)

def insert_email(email):
    emails.insert_one(email)

def find_user(email):
    return users.find_one({"email": email})

def find_task(email, description):
    return tasks.find_one({"user_email": email, "description": description})

def find_email(email, subject):
    return emails.find_one({"user_email": email, "subject": subject})

def update_user(email, update):
    users.update_one({"email": email}, {"$set": update})

def update_task(email, description, update):
    tasks.update_one({"user_email": email, "description": description}, {"$set": update})

def update_email(email, subject, update):
    emails.update_one({"user_email": email, "subject": subject}, {"$set": update})

def delete_user(email):
    users.delete_one({"email": email})

def delete_task(email, description):
    tasks.delete_one({"user_email": email, "description": description})

def delete_email(email, subject):
    emails.delete_one({"user_email": email, "subject": subject})
```