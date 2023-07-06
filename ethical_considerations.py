import json

class EthicalConsiderations:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def consider_ethics(self, meeting_data):
        ethical_issues = self.identify_ethical_issues(meeting_data)
        if ethical_issues:
            self.notify_user(ethical_issues)

    def identify_ethical_issues(self, meeting_data):
        ethical_issues = []
        for meeting in meeting_data:
            if meeting['duration'] > self.user_profile['max_meeting_duration']:
                ethical_issues.append(f"Meeting {meeting['id']} exceeds maximum duration.")
            if meeting['participants'] > self.user_profile['max_participants']:
                ethical_issues.append(f"Meeting {meeting['id']} exceeds maximum participants.")
        return ethical_issues

    def notify_user(self, ethical_issues):
        notification = {
            'type': 'ethical_issues',
            'message': '\n'.join(ethical_issues)
        }
        with open('ai_assistant/email_notifications.py', 'a') as file:
            file.write(json.dumps(notification))

if __name__ == "__main__":
    user_profile = {
        'max_meeting_duration': 60,
        'max_participants': 10
    }
    meeting_data = [
        {'id': 1, 'duration': 120, 'participants': 12},
        {'id': 2, 'duration': 30, 'participants': 5}
    ]
    ethical_considerations = EthicalConsiderations(user_profile)
    ethical_considerations.consider_ethics(meeting_data)