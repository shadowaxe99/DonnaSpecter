```python
import requests
from bs4 import BeautifulSoup

class SocialMediaManagement:
    def __init__(self):
        self.social_media_platforms = ['LinkedIn', 'Twitter', 'Facebook']
        self.posts = []

    def fetch_posts(self, platform):
        if platform in self.social_media_platforms:
            # This is a placeholder for actual API calls to fetch posts
            # Replace with actual API calls based on the platform
            response = requests.get(f'https://api.{platform}.com/posts')
            self.posts = response.json()
        else:
            print(f"{platform} is not supported.")

    def create_post(self, platform, content):
        if platform in self.social_media_platforms:
            # This is a placeholder for actual API calls to create posts
            # Replace with actual API calls based on the platform
            response = requests.post(f'https://api.{platform}.com/posts', data=content)
            if response.status_code == 200:
                print("Post created successfully.")
            else:
                print("Failed to create post.")
        else:
            print(f"{platform} is not supported.")

    def delete_post(self, platform, post_id):
        if platform in self.social_media_platforms:
            # This is a placeholder for actual API calls to delete posts
            # Replace with actual API calls based on the platform
            response = requests.delete(f'https://api.{platform}.com/posts/{post_id}')
            if response.status_code == 200:
                print("Post deleted successfully.")
            else:
                print("Failed to delete post.")
        else:
            print(f"{platform} is not supported.")

    def update_post(self, platform, post_id, new_content):
        if platform in self.social_media_platforms:
            # This is a placeholder for actual API calls to update posts
            # Replace with actual API calls based on the platform
            response = requests.put(f'https://api.{platform}.com/posts/{post_id}', data=new_content)
            if response.status_code == 200:
                print("Post updated successfully.")
            else:
                print("Failed to update post.")
        else:
            print(f"{platform} is not supported.")
```