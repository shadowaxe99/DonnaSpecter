import datetime
from ai_assistant.shared_dependencies import UserProfileSchema, LearningSchema

class LearningDevelopment:
    def __init__(self, user_profile: UserProfileSchema, learning_data: LearningSchema):
        self.user_profile = user_profile
        self.learning_data = learning_data

    def update_learning_progress(self, new_progress):
        self.learning_data.progress = new_progress
        self.learning_data.last_updated = datetime.datetime.now()

    def recommend_learning_path(self):
        if self.user_profile.job_role == 'Developer':
            return 'AI and Machine Learning'
        elif self.user_profile.job_role == 'Project Manager':
            return 'Agile and Scrum'
        else:
            return 'Communication Skills'

    def set_learning_goals(self, new_goals):
        self.learning_data.goals = new_goals

    def track_learning_progress(self):
        progress = self.learning_data.progress
        goals = self.learning_data.goals
        if progress >= goals:
            return 'Learning goal achieved!'
        else:
            return f'Keep going! You are {goals - progress}% away from your goal.'

    def get_learning_summary(self):
        return {
            'user': self.user_profile.name,
            'progress': self.learning_data.progress,
            'goals': self.learning_data.goals,
            'recommended_path': self.recommend_learning_path()
        }