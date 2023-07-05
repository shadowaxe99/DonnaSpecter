```python
import pandas as pd
from datetime import datetime

class ExpenseManagement:
    def __init__(self, user_profile, expense_data):
        self.user_profile = user_profile
        self.expense_data = expense_data

    def load_expenses(self):
        self.expenses = pd.read_csv(self.expense_data)

    def categorize_expenses(self):
        self.expenses['category'] = self.expenses['description'].apply(self._get_category)

    def _get_category(self, description):
        # This function can be improved with NLP for better categorization
        if 'travel' in description.lower():
            return 'Travel'
        elif 'food' in description.lower():
            return 'Food'
        else:
            return 'Other'

    def calculate_monthly_expenses(self):
        self.expenses['date'] = pd.to_datetime(self.expenses['date'])
        self.expenses['month'] = self.expenses['date'].dt.month
        monthly_expenses = self.expenses.groupby('month').sum()
        return monthly_expenses

    def alert_if_over_budget(self):
        monthly_expenses = self.calculate_monthly_expenses()
        for month, expense in monthly_expenses.items():
            if expense > self.user_profile['budget']:
                print(f'Alert: You are over budget for month {month} by {expense - self.user_profile["budget"]}')

if __name__ == "__main__":
    user_profile = {'budget': 1000}
    expense_manager = ExpenseManagement(user_profile, 'expense_data.csv')
    expense_manager.load_expenses()
    expense_manager.categorize_expenses()
    expense_manager.alert_if_over_budget()
```