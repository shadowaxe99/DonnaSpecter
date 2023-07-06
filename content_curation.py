import os
import json
from ai_assistant.shared_dependencies import user_profile, content_data

class ContentCuration:
    def __init__(self, user_profile, content_data):
        self.user_profile = user_profile
        self.content_data = content_data

    def curate_content(self):
        curated_content = []
        for content in self.content_data:
            if self.user_profile['interests'] in content['tags']:
                curated_content.append(content)
        return curated_content

    def save_curated_content(self, curated_content):
        with open('curated_content.json', 'w') as json_file:
            json.dump(curated_content, json_file)

    def load_curated_content(self):
        if os.path.exists('curated_content.json'):
            with open('curated_content.json') as json_file:
                curated_content = json.load(json_file)
            return curated_content
        else:
            return []

if __name__ == "__main__":
    content_curation = ContentCuration(user_profile, content_data)
    curated_content = content_curation.curate_content()
    content_curation.save_curated_content(curated_content)
    loaded_content = content_curation.load_curated_content()
    print(loaded_content)