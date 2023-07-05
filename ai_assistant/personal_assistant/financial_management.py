```python
import json
from datetime import datetime
from ai_assistant.shared_dependencies import user_profile, app_settings, api_keys
from ai_assistant.shared_dependencies import UserSchema, TaskSchema, ContactSchema
from ai_assistant.shared_dependencies import updateUserProfile, updateTask, updateContact

class FinancialManagement:
    def __init__(self):
        self.user_financial_data = user_profile.get('financial_data', {})

    def update_financial_data(self, new_data):
        self.user_financial_data.update(new_data)
        user_profile['financial_data'] = self.user_financial_data
        updateUserProfile(user_profile)

    def get_financial_summary(self):
        return self.user_financial_data.get('summary', {})

    def add_expense(self, category, amount, date=None):
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
        expense = {
            'category': category,
            'amount': amount,
            'date': date
        }
        self.user_financial_data.setdefault('expenses', []).append(expense)
        self.update_financial_data(self.user_financial_data)

    def add_income(self, source, amount, date=None):
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
        income = {
            'source': source,
            'amount': amount,
            'date': date
        }
        self.user_financial_data.setdefault('income', []).append(income)
        self.update_financial_data(self.user_financial_data)

    def generate_financial_report(self):
        report = {
            'summary': self.get_financial_summary(),
            'expenses': self.user_financial_data.get('expenses', []),
            'income': self.user_financial_data.get('income', [])
        }
        return json.dumps(report, indent=4)

financial_management = FinancialManagement()
```