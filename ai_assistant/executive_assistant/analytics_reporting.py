```python
import pandas as pd
from datetime import datetime
from ai_assistant.shared_dependencies import user_profile, app_settings, api_keys

class AnalyticsReporting:
    def __init__(self):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def generate_report(self, data, report_type):
        if report_type == 'csv':
            self.generate_csv_report(data)
        elif report_type == 'json':
            self.generate_json_report(data)
        else:
            print("Invalid report type. Please choose 'csv' or 'json'.")

    def generate_csv_report(self, data):
        df = pd.DataFrame(data)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{self.user_profile['username']}_report_{timestamp}.csv"
        df.to_csv(filename, index=False)
        print(f"CSV report generated: {filename}")

    def generate_json_report(self, data):
        df = pd.DataFrame(data)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{self.user_profile['username']}_report_{timestamp}.json"
        df.to_json(filename)
        print(f"JSON report generated: {filename}")

analytics_reporting = AnalyticsReporting()
```
