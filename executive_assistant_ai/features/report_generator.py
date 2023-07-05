```python
import pandas as pd
from executive_assistant_ai.utils import data_cleaner, data_validator, logger

class ReportGenerator:
    def __init__(self):
        self.logger = logger.Logger("ReportGenerator")

    def generate_report(self, data, report_type):
        self.logger.log("Generating report...")

        cleaned_data = data_cleaner.clean(data)
        if not data_validator.validate(cleaned_data):
            self.logger.log("Invalid data, cannot generate report.")
            return None

        if report_type == "summary":
            return self._generate_summary_report(cleaned_data)
        elif report_type == "detailed":
            return self._generate_detailed_report(cleaned_data)
        else:
            self.logger.log("Invalid report type.")
            return None

    def _generate_summary_report(self, data):
        self.logger.log("Generating summary report...")
        summary = data.describe()
        return summary

    def _generate_detailed_report(self, data):
        self.logger.log("Generating detailed report...")
        detailed_report = data.groupby(['Category']).sum().sort_values('Amount', ascending=False)
        return detailed_report
```