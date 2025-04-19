from .repositories import get_mock_twitter_posts, get_mock_reddit_posts, get_mock_news_articles
from typing import Dict, Any

def fetch_twitter_posts(company_name: str) -> Dict[str, Any]:
    return {"twitter_posts": get_mock_twitter_posts(company_name)}

def fetch_reddit_posts(company_name: str) -> Dict[str, Any]:
    return {"twitter_posts": get_mock_reddit_posts(company_name)}

def fetch_news_articles(company_name: str) -> Dict[str, Any]:
    return {"twitter_posts": get_mock_news_articles(company_name)}
