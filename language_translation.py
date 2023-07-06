import requests
from shared_dependencies import user_profile, meeting_data

class LanguageTranslation:
    def __init__(self):
        self.api_key = "YOUR_TRANSLATION_API_KEY"
        self.url = "https://api.translationapi.com/v1.5/tr"

    def translate_text(self, text, target_language):
        data = {
            "q": text,
            "target": target_language
        }
        headers = {
            "Authorization": "Bearer " + self.api_key
        }
        response = requests.post(self.url, headers=headers, data=data)
        return response.json()["data"]["translations"][0]["translatedText"]

    def translate_meeting_data(self):
        for meeting in meeting_data:
            if meeting["language"] != user_profile["preferred_language"]:
                meeting["title"] = self.translate_text(meeting["title"], user_profile["preferred_language"])
                meeting["description"] = self.translate_text(meeting["description"], user_profile["preferred_language"])
        return meeting_data

language_translation = LanguageTranslation()
translated_meeting_data = language_translation.translate_meeting_data()