```python
import requests
import json

UBER_EATS_API_KEY = 'your_ubereats_api_key'
GOPUFF_API_KEY = 'your_gopuff_api_key'

class FoodDelivery:
    def __init__(self):
        self.headers = {
            'UberEats': {'Authorization': 'Bearer ' + UBER_EATS_API_KEY},
            'GoPuff': {'Authorization': 'Bearer ' + GOPUFF_API_KEY}
        }

    def get_restaurants(self, service, location):
        if service == 'UberEats':
            url = f'https://api.ubereats.com/v1/restaurants?location={location}'
        elif service == 'GoPuff':
            url = f'https://api.gopuff.com/v1/restaurants?location={location}'
        else:
            return 'Invalid service'

        response = requests.get(url, headers=self.headers[service])
        return response.json()

    def order_food(self, service, restaurant_id, food_id):
        if service == 'UberEats':
            url = f'https://api.ubereats.com/v1/order?restaurant_id={restaurant_id}&food_id={food_id}'
        elif service == 'GoPuff':
            url = f'https://api.gopuff.com/v1/order?restaurant_id={restaurant_id}&food_id={food_id}'
        else:
            return 'Invalid service'

        response = requests.post(url, headers=self.headers[service])
        return response.json()

food_delivery = FoodDelivery()
print(food_delivery.get_restaurants('UberEats', 'San Francisco'))
print(food_delivery.order_food('GoPuff', '123', '456'))
```