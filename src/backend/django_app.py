```python
from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Task, Email
from src.security.encryption import encryptData, decryptData
from src.database.postgresql import connectDB

USER_EMAIL = "user@example.com"
USER_CREDENTIALS = "user_credentials"

def home(request):
    return render(request, 'home.html')

def handleEmail(request):
    if request.method == 'POST':
        email_data = request.POST
        encrypted_data = encryptData(email_data)
        email = Email(email_data=encrypted_data)
        email.save()
        return JsonResponse({"message": "EMAIL_RECEIVED"}, status=200)

def scheduleTask(request):
    if request.method == 'POST':
        task_data = request.POST
        encrypted_data = encryptData(task_data)
        task = Task(task_data=encrypted_data)
        task.save()
        return JsonResponse({"message": "TASK_SCHEDULED"}, status=200)

def getUserData(request):
    if request.method == 'GET':
        user = User.objects.get(email=USER_EMAIL)
        decrypted_data = decryptData(user.data)
        return JsonResponse({"data": decrypted_data}, status=200)

def updateUserData(request):
    if request.method == 'POST':
        user_data = request.POST
        encrypted_data = encryptData(user_data)
        User.objects.filter(email=USER_EMAIL).update(data=encrypted_data)
        return JsonResponse({"message": "User data updated"}, status=200)

def connectToDB(request):
    connection = connectDB()
    if connection:
        return JsonResponse({"message": "Database connected"}, status=200)
    else:
        return JsonResponse({"message": "Database connection failed"}, status=500)
```