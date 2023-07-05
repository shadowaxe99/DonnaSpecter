```python
import requests
import json

NEWS_API_KEY = "your_news_api_key"

def fetch_news():
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
    news = response.json()
    return news['articles']

def filter_news(news, interest):
    filtered_news = [article for article in news if interest in article['title']]
    return filtered_news

def display_news(news):
    for article in news:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("\n")

if __name__ == "__main__":
    news = fetch_news()
    interest = "technology"
    filtered_news = filter_news(news, interest)
    display_news(filtered_news)
```