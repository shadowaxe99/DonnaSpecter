```python
import re

class DataValidator:
    def __init__(self):
        pass

    def validate_email(self, email):
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(email_regex,email)):  
            return True  
        else:  
            return False

    def validate_date(self, date):
        date_regex = '^(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/[0-9]{4}$'
        if(re.search(date_regex,date)):  
            return True  
        else:  
            return False

    def validate_time(self, time):
        time_regex = '^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
        if(re.search(time_regex,time)):  
            return True  
        else:  
            return False

    def validate_phone(self, phone):
        phone_regex = '^[+]?[0-9]{1,4}?[-.]?[0-9]{1,8}$'
        if(re.search(phone_regex,phone)):  
            return True  
        else:  
            return False

    def validate_text(self, text):
        if len(text) > 0:
            return True
        else:
            return False
```