```python
import requests
from schemas import UserSchema

class RideOrdering:
    def __init__(self, user_profile, api_keys):
        self.user_profile = user_profile
        self.api_key = api_keys['uber']

    def order_ride(self, destination):
        headers = {
            'Authorization': 'Bearer %s' % self.api_key,
            'Content-Type': 'application/json',
        }

        params = (
            ('start_latitude', self.user_profile['location']['latitude']),
            ('start_longitude', self.user_profile['location']['longitude']),
            ('end_latitude', destination['latitude']),
            ('end_longitude', destination['longitude']),
        )

        response = requests.get('https://api.uber.com/v1.2/requests/estimate', headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Unable to order ride')

def updateUserProfile(new_profile):
    global user_profile
    user_profile = UserSchema().load(new_profile)
    return user_profile

def updateApiKey(new_key):
    global api_keys
    api_keys['uber'] = new_key
    return api_keys
```