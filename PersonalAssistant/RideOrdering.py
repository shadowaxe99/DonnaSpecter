```python
import requests
import os

UBER_API_KEY = os.getenv('UBER_API_KEY')

def get_price_estimates(start_latitude, start_longitude, end_latitude, end_longitude):
    url = "https://api.uber.com/v1.2/estimates/price"
    headers = {
        'Authorization': 'Bearer %s' % UBER_API_KEY,
        'Content-Type': 'application/json',
    }
    params = {
        'start_latitude': start_latitude,
        'start_longitude': start_longitude,
        'end_latitude': end_latitude,
        'end_longitude': end_longitude,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_time_estimates(start_latitude, start_longitude):
    url = "https://api.uber.com/v1.2/estimates/time"
    headers = {
        'Authorization': 'Bearer %s' % UBER_API_KEY,
        'Content-Type': 'application/json',
    }
    params = {
        'start_latitude': start_latitude,
        'start_longitude': start_longitude,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def request_ride(product_id, start_latitude, start_longitude, end_latitude, end_longitude):
    url = "https://api.uber.com/v1.2/requests"
    headers = {
        'Authorization': 'Bearer %s' % UBER_API_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'product_id': product_id,
        'start_latitude': start_latitude,
        'start_longitude': start_longitude,
        'end_latitude': end_latitude,
        'end_longitude': end_longitude,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
```