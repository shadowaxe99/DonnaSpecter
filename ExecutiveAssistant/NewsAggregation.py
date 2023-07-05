```python
import requests
from typing import List, Dict

NEWS_API_KEY = "your_news_api_key"

def fetch_news() -> List[Dict]:
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_API_KEY}")
    data = response.json()
    return data["articles"]

def filter_news(articles: List[Dict], keyword: str) -> List[Dict]:
    filtered_articles = [article for article in articles if keyword.lower() in article["title"].lower()]
    return filtered_articles

def display_news(articles: List[Dict]) -> None:
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("\n")

if __name__ == "__main__":
    articles = fetch_news()
    filtered_articles = filter_news(articles, "market")
    display_news(filtered_articles)
```