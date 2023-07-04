```python
import json

class MeetingTemplate:
    def __init__(self, template_id, template_name, template_details):
        self.template_id = template_id
        self.template_name = template_name
        self.template_details = template_details

    def get_template_id(self):
        return self.template_id

    def get_template_name(self):
        return self.template_name

    def get_template_details(self):
        return self.template_details

    def set_template_details(self, template_details):
        self.template_details = template_details

class MeetingTemplatesManager:
    def __init__(self):
        self.templates = []

    def load_templates(self, file_path):
        with open(file_path, 'r') as file:
            templates_data = json.load(file)
            for template_data in templates_data:
                template = MeetingTemplate(template_data['id'], template_data['name'], template_data['details'])
                self.templates.append(template)

    def save_templates(self, file_path):
        templates_data = []
        for template in self.templates:
            template_data = {
                'id': template.get_template_id(),
                'name': template.get_template_name(),
                'details': template.get_template_details()
            }
            templates_data.append(template_data)

        with open(file_path, 'w') as file:
            json.dump(templates_data, file)

    def create_template(self, template_name, template_details):
        template_id = len(self.templates) + 1
        template = MeetingTemplate(template_id, template_name, template_details)
        self.templates.append(template)

    def get_template(self, template_id):
        for template in self.templates:
            if template.get_template_id() == template_id:
                return template
        return None

    def update_template(self, template_id, template_details):
        template = self.get_template(template_id)
        if template is not None:
            template.set_template_details(template_details)

    def delete_template(self, template_id):
        template = self.get_template(template_id)
        if template is not None:
            self.templates.remove(template)
```
