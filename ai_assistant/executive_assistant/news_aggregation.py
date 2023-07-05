```python
import requests
from bs4 import BeautifulSoup

class NewsAggregator:
    def __init__(self, user_profile, app_settings, api_keys):
        self.user_profile = user_profile
        self.app_settings = app_settings
        self.api_keys = api_keys

    def fetch_news(self, source):
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2')
        return [headline.text for headline in headlines]

    def aggregate_news(self):
        news_sources = self.app_settings.get('news_sources', [])
        aggregated_news = []
        for source in news_sources:
            aggregated_news.extend(self.fetch_news(source))
        return aggregated_news

    def update_news(self):
        aggregated_news = self.aggregate_news()
        self.user_profile['news'] = aggregated_news
        return self.user_profile

    def display_news(self):
        news = self.user_profile.get('news', [])
        for headline in news:
            print(headline)

if __name__ == "__main__":
    user_profile = {}  # Fetch from UserSchema
    app_settings = {}  # Fetch from app settings
    api_keys = {}  # Fetch from secure storage

    news_aggregator = NewsAggregator(user_profile, app_settings, api_keys)
    news_aggregator.update_news()
    news_aggregator.display_news()
```