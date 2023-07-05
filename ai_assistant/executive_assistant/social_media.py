```python
import requests
from schemas import UserSchema

class SocialMedia:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def update_social_media(self, platform, status):
        if platform.lower() == "twitter":
            self.post_twitter(status)
        elif platform.lower() == "facebook":
            self.post_facebook(status)
        elif platform.lower() == "linkedin":
            self.post_linkedin(status)
        else:
            print("Invalid platform")

    def post_twitter(self, status):
        twitter_api_key = self.api_keys['twitter']
        # Code to post status on Twitter using twitter_api_key

    def post_facebook(self, status):
        facebook_api_key = self.api_keys['facebook']
        # Code to post status on Facebook using facebook_api_key

    def post_linkedin(self, status):
        linkedin_api_key = self.api_keys['linkedin']
        # Code to post status on LinkedIn using linkedin_api_key

def updateUserProfile(user_profile):
    user_schema = UserSchema()
    validated_user_profile = user_schema.load(user_profile)
    social_media = SocialMedia(validated_user_profile, app_settings, api_keys)
    return social_media
```