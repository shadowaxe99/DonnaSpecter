```python
import requests
from schemas import TaskSchema

class FoodDelivery:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def order_food(self, restaurant_id, menu_item_id):
        url = f"https://api.ubereats.com/v1/restaurants/{restaurant_id}/menu_items/{menu_item_id}/order"
        headers = {"Authorization": f"Bearer {self.api_keys['uber_eats']}"}
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            order_id = response.json()['order_id']
            self.update_task(order_id)
            return order_id
        else:
            raise Exception("Order failed")

    def update_task(self, order_id):
        task = {
            "id": order_id,
            "type": "food_delivery",
            "status": "ordered",
            "user_id": self.user_profile['id']
        }
        task_schema = TaskSchema()
        valid_task = task_schema.load(task)
        updateTask(valid_task)

    def check_order_status(self, order_id):
        url = f"https://api.ubereats.com/v1/orders/{order_id}"
        headers = {"Authorization": f"Bearer {self.api_keys['uber_eats']}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()['status']
        else:
            raise Exception("Failed to get order status")
```