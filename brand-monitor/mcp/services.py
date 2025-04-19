"""Service layer for fetching posts and articles from repositories.

Returns:
    dict: Dictionary containing lists of posts/articles for each source.
"""
from .repositories import get_mock_twitter_posts, get_mock_reddit_posts, get_mock_news_articles
from typing import Dict, Any

def fetch_twitter_posts(company_name: str) -> Dict[str, Any]:
    """Fetch Twitter posts for a specified company.

    Args:
        company_name (str): The company name to search tweets for.

    Returns:
        Dict[str, Any]: Dictionary with key 'twitter_posts' and list of posts as value.
    """
    return {"twitter_posts": get_mock_twitter_posts(company_name)}

def fetch_reddit_posts(company_name: str) -> Dict[str, Any]:
    """Fetch Reddit posts for a specified company.

    Args:
        company_name (str): The company name to search Reddit posts for.

    Returns:
        Dict[str, Any]: Dictionary with key 'reddit_posts' and list of posts as value.
    """
    return {"reddit_posts": get_mock_reddit_posts(company_name)}

def fetch_news_articles(company_name: str) -> Dict[str, Any]:
    """Fetch news articles for a specified company.

    Args:
        company_name (str): The company name to search news articles for.

    Returns:
        Dict[str, Any]: Dictionary with key 'news_articles' and list of articles as value.
    """
    return {"news_articles": get_mock_news_articles(company_name)}
