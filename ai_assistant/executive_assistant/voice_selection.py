```python
import pyttsx3

class VoiceSelection:
    def __init__(self, user_profile, app_settings):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.engine = pyttsx3.init()

    def get_voices(self):
        voices = self.engine.getProperty('voices')
        return voices

    def set_voice(self, voice_id):
        self.engine.setProperty('voice', voice_id)
        self.app_settings['voice_id'] = voice_id

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def update_user_profile(self, user_profile):
        self.user_profile = user_profile
        if 'voice_id' in user_profile:
            self.set_voice(user_profile['voice_id'])

if __name__ == "__main__":
    user_profile = {}  # Fetch from user data
    app_settings = {}  # Fetch from app settings
    voice_selection = VoiceSelection(user_profile, app_settings)
    voices = voice_selection.get_voices()
    # Display voices to user and let them select
    selected_voice_id = voices[0].id  # Assume user selects the first voice
    voice_selection.set_voice(selected_voice_id)
    voice_selection.speak("Voice has been set successfully.")
```
