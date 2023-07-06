import json
import requests
from datetime import datetime

from shared_dependencies import UserProfileSchema, MeetingSchema

class ZoomInvite:
    def __init__(self, user_profile: UserProfileSchema, meeting_data: MeetingSchema):
        self.user_profile = user_profile
        self.meeting_data = meeting_data

    def generate_zoom_invite(self):
        zoom_api_url = "https://api.zoom.us/v2/users/{}/meetings".format(self.user_profile.zoom_user_id)

        headers = {
            "Authorization": "Bearer {}".format(self.user_profile.zoom_jwt_token),
            "Content-Type": "application/json"
        }

        meeting_time = datetime.strptime(self.meeting_data.date_time, "%Y-%m-%dT%H:%M:%S")

        payload = {
            "topic": self.meeting_data.topic,
            "type": 2,
            "start_time": meeting_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "duration": self.meeting_data.duration,
            "timezone": self.user_profile.timezone,
            "settings": {
                "host_video": self.meeting_data.host_video,
                "participant_video": self.meeting_data.participant_video,
                "join_before_host": self.meeting_data.join_before_host,
                "mute_upon_entry": self.meeting_data.mute_upon_entry,
                "waiting_room": self.meeting_data.waiting_room,
                "auto_recording": self.meeting_data.auto_recording
            }
        }

        response = requests.post(zoom_api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 201:
            return response.json()["join_url"]
        else:
            raise Exception("Failed to create Zoom invite. Error: {}".format(response.text))

zoom_invite = ZoomInvite(user_profile, meeting_data)
zoom_link = zoom_invite.generate_zoom_invite()