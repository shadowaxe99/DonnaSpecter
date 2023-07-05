```python
import requests
from datetime import datetime

class LearningDevelopment:
    def __init__(self, user_id):
        self.user_id = user_id
        self.courses = []
        self.webinars = []

    def fetch_courses(self, topic):
        response = requests.get(f"https://api.courses.com/{topic}")
        self.courses = response.json()

    def fetch_webinars(self, topic):
        response = requests.get(f"https://api.webinars.com/{topic}")
        self.webinars = response.json()

    def enroll_course(self, course_id):
        response = requests.post(f"https://api.courses.com/enroll/{course_id}", data={"user_id": self.user_id})
        return response.status_code == 200

    def register_webinar(self, webinar_id):
        response = requests.post(f"https://api.webinars.com/register/{webinar_id}", data={"user_id": self.user_id})
        return response.status_code == 200

    def get_upcoming_courses(self):
        upcoming_courses = [course for course in self.courses if datetime.strptime(course['start_date'], '%Y-%m-%d') > datetime.now()]
        return upcoming_courses

    def get_upcoming_webinars(self):
        upcoming_webinars = [webinar for webinar in self.webinars if datetime.strptime(webinar['start_date'], '%Y-%m-%d') > datetime.now()]
        return upcoming_webinars
```