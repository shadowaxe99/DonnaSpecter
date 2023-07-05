```python
import requests
from dotenv import load_dotenv
import os

load_dotenv()

SUBSCRIPTION_API_KEY = os.getenv('SUBSCRIPTION_API_KEY')
SUBSCRIPTION_API_SECRET = os.getenv('SUBSCRIPTION_API_SECRET')

class SubscriptionManagement:
    def __init__(self):
        self.api_key = SUBSCRIPTION_API_KEY
        self.api_secret = SUBSCRIPTION_API_SECRET

    def add_subscription(self, subscription_name, subscription_cost, subscription_date):
        payload = {
            'name': subscription_name,
            'cost': subscription_cost,
            'date': subscription_date
        }
        response = requests.post('https://subscriptionapi.com/add', data=payload, auth=(self.api_key, self.api_secret))
        return response.json()

    def remove_subscription(self, subscription_id):
        response = requests.delete(f'https://subscriptionapi.com/remove/{subscription_id}', auth=(self.api_key, self.api_secret))
        return response.json()

    def update_subscription(self, subscription_id, subscription_name=None, subscription_cost=None, subscription_date=None):
        payload = {
            'name': subscription_name,
            'cost': subscription_cost,
            'date': subscription_date
        }
        response = requests.put(f'https://subscriptionapi.com/update/{subscription_id}', data=payload, auth=(self.api_key, self.api_secret))
        return response.json()

    def list_subscriptions(self):
        response = requests.get('https://subscriptionapi.com/list', auth=(self.api_key, self.api_secret))
        return response.json()

if __name__ == "__main__":
    sm = SubscriptionManagement()
    print(sm.add_subscription('Netflix', 15, '2022-01-01'))
    print(sm.list_subscriptions())
    print(sm.update_subscription(1, subscription_cost=20))
    print(sm.remove_subscription(1))
```