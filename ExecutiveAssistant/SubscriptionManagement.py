```python
import os
from subscription_api import SubscriptionAPI

# Exported variables
SUBSCRIPTION_API_KEY = os.getenv('SUBSCRIPTION_API_KEY')
SUBSCRIPTION_API_SECRET = os.getenv('SUBSCRIPTION_API_SECRET')

# Initialize Subscription API
subscription_api = SubscriptionAPI(SUBSCRIPTION_API_KEY, SUBSCRIPTION_API_SECRET)

def add_subscription(subscription):
    """
    Add a new subscription
    """
    response = subscription_api.add_subscription(subscription)
    return response

def remove_subscription(subscription_id):
    """
    Remove a subscription
    """
    response = subscription_api.remove_subscription(subscription_id)
    return response

def update_subscription(subscription_id, subscription):
    """
    Update a subscription
    """
    response = subscription_api.update_subscription(subscription_id, subscription)
    return response

def list_subscriptions():
    """
    List all subscriptions
    """
    response = subscription_api.list_subscriptions()
    return response
```