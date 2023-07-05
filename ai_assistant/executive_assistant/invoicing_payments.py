```python
import requests
from schemas import UserSchema, TaskSchema

class InvoicingPayments:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def create_invoice(self, task):
        # Validate task schema
        TaskSchema.validate(task)

        # Create invoice
        invoice_data = {
            "user": self.user_profile,
            "task": task,
            "api_key": self.api_keys['invoice_api']
        }

        response = requests.post(self.app_settings['invoice_url'], data=invoice_data)

        if response.status_code == 200:
            print("Invoice created successfully.")
        else:
            print("Failed to create invoice.")

    def make_payment(self, invoice_id):
        # Make payment
        payment_data = {
            "user": self.user_profile,
            "invoice_id": invoice_id,
            "api_key": self.api_keys['payment_api']
        }

        response = requests.post(self.app_settings['payment_url'], data=payment_data)

        if response.status_code == 200:
            print("Payment made successfully.")
        else:
            print("Failed to make payment.")
```