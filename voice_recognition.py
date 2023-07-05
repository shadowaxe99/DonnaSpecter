```python
import speech_recognition as sr

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except:
                print("Sorry, I did not get that")
                return None

    def recognize_voice(self, command):
        if 'schedule' in command:
            from ai_assistant.scheduler import schedule
            schedule()
        elif 'zoom invite' in command:
            from ai_assistant.zoom_invites import zoomInvite
            zoomInvite()
        elif 'google meet' in command:
            from ai_assistant.google_meets import googleMeet
            googleMeet()
        elif 'email notification' in command:
            from ai_assistant.email_notifications import emailNotification
            emailNotification()
        # Add more elif conditions for other commands
        else:
            print("Command not recognized")

if __name__ == "__main__":
    vr = VoiceRecognition()
    while True:
        command = vr.listen()
        if command:
            vr.recognize_voice(command)
```
This Python script uses the SpeechRecognition library to listen to the user's voice and convert it into text. It then checks if the text contains certain keywords and calls the corresponding function from the appropriate file. If the command is not recognized, it prints a message to the user. The script runs in an infinite loop, continuously listening for commands.