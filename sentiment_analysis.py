```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Import shared dependencies
from shared_dependencies import user_profile, meeting_data

class SentimentAnalysis:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_score = self.sia.polarity_scores(text)
        return sentiment_score

    def analyze_meeting_sentiment(self, meeting_id):
        meeting = meeting_data[meeting_id]
        meeting_text = meeting['transcript']
        sentiment_score = self.analyze_sentiment(meeting_text)
        return sentiment_score

    def analyze_user_sentiment(self, user_id):
        user = user_profile[user_id]
        user_text = user['communication_history']
        sentiment_score = self.analyze_sentiment(user_text)
        return sentiment_score

# Initialize sentiment analysis
sentiment_analysis = SentimentAnalysis()

# Analyze sentiment for a specific meeting
meeting_sentiment = sentiment_analysis.analyze_meeting_sentiment('meeting123')

# Analyze sentiment for a specific user
user_sentiment = sentiment_analysis.analyze_user_sentiment('user123')
```