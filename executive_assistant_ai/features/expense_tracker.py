```python
import datetime
from executive_assistant_ai.utils.data_validator import validate_expense_data
from executive_assistant_ai.utils.error_handler import handle_error
from executive_assistant_ai.utils.logger import log

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense_data):
        try:
            if validate_expense_data(expense_data):
                self.expenses.append(expense_data)
                log(f"Expense added: {expense_data}")
            else:
                raise ValueError("Invalid expense data")
        except Exception as e:
            handle_error(e)

    def get_expenses(self, start_date=None, end_date=None):
        if start_date is None:
            start_date = datetime.datetime.min
        if end_date is None:
            end_date = datetime.datetime.max

        return [expense for expense in self.expenses if start_date <= expense['date'] <= end_date]

    def get_total_expenses(self, start_date=None, end_date=None):
        expenses = self.get_expenses(start_date, end_date)
        return sum(expense['amount'] for expense in expenses)
```