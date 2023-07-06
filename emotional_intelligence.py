import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ai_assistant.shared_dependencies import user_profile, meeting_data

class EmotionalIntelligence:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.emotion_labels = ['happy', 'sad', 'angry', 'neutral', 'surprised']

    def train_model(self, emotion_data, labels):
        self.model.fit(emotion_data, labels)

    def predict_emotion(self, data):
        return self.model.predict(np.array(data).reshape(1, -1))

    def analyze_emotion(self, user_id):
        user = user_profile[user_id]
        emotion_data = user['emotion_data']
        predicted_emotion = self.predict_emotion(emotion_data)
        return self.emotion_labels[predicted_emotion[0]]

    def adjust_meeting_based_on_emotion(self, user_id, meeting_id):
        emotion = self.analyze_emotion(user_id)
        meeting = meeting_data[meeting_id]

        if emotion == 'happy':
            meeting['duration'] += 10
        elif emotion == 'sad':
            meeting['duration'] -= 10
        elif emotion == 'angry':
            meeting['duration'] -= 15
        elif emotion == 'surprised':
            meeting['duration'] += 5

        return meeting