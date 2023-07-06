import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Importing shared dependencies
from shared_dependencies import user_profile, meeting_data

class ContextUnderstanding:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def tokenize(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokenized_text):
        return [word for word in tokenized_text if word not in self.stop_words]

    def understand_context(self, text):
        tokenized = self.tokenize(text)
        tokenized = self.remove_stopwords(tokenized)

        tagged = nltk.pos_tag(tokenized)

        namedEnt = nltk.ne_chunk(tagged)
        namedEnt.draw()

        return namedEnt

context_understanding = ContextUnderstanding()

def update_context():
    for meeting in meeting_data:
        context = context_understanding.understand_context(meeting['description'])
        meeting['context'] = context

def get_context(user_id):
    user_meetings = [meeting for meeting in meeting_data if meeting['user_id'] == user_id]
    user_context = [meeting['context'] for meeting in user_meetings]
    return user_context