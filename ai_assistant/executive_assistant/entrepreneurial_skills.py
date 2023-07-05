```python
import json
from ai_assistant.shared import user_profile, app_settings, api_keys
from ai_assistant.shared import UserSchema, TaskSchema, ContactSchema
from ai_assistant.shared import updateUserProfile, updateTask, updateContact

class EntrepreneurialSkills:
    def __init__(self):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def update_skills(self, new_skills):
        self.user_profile['entrepreneurial_skills'] = new_skills
        updateUserProfile(self.user_profile)

    def get_skills(self):
        return self.user_profile.get('entrepreneurial_skills', [])

    def add_skill(self, skill):
        current_skills = self.get_skills()
        if skill not in current_skills:
            current_skills.append(skill)
            self.update_skills(current_skills)

    def remove_skill(self, skill):
        current_skills = self.get_skills()
        if skill in current_skills:
            current_skills.remove(skill)
            self.update_skills(current_skills)

    def has_skill(self, skill):
        return skill in self.get_skills()

if __name__ == "__main__":
    entrepreneurial_skills = EntrepreneurialSkills()
    entrepreneurial_skills.add_skill('Risk Management')
    entrepreneurial_skills.add_skill('Business Strategy')
    print(entrepreneurial_skills.get_skills())
    entrepreneurial_skills.remove_skill('Risk Management')
    print(entrepreneurial_skills.get_skills())
```