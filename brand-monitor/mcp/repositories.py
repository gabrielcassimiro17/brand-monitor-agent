"""Repositories for fetching mock posts from various sources.

Returns:
    list[dict]: List of post/article dictionaries for each source.
"""

from typing import List, Dict, Any
import os
import praw
from datetime import datetime
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "brand-monitor-agent")


def get_mock_twitter_posts(company_name: str) -> List[Dict[str, Any]]:
    """Fetch mock Twitter posts for a company.

    Args:
        company_name (str): The company name to search tweets for.

    Returns:
        List[Dict[str, Any]]: List of mock Twitter post dictionaries.
    """
    return [
        {
            "id": "tweet_123",
            "text": "Excited about the new features announced at Google I/O! #GoogleIO #AI",
            "author": "TechEnthusiast",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "twitter",
            "company_query": company_name,
        },
        {
            "id": "tweet_456",
            "text": "Google's latest algorithm update seems to be rolling out. Seeing some ranking changes.",
            "author": "SEOGuru",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "twitter",
            "company_query": company_name,
        },
        {
            "id": "tweet_789",
            "text": "Using Google Workspace for collaboration is seamless. Highly recommend!",
            "author": "RemoteWorker",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "twitter",
            "company_query": company_name,
        },
    ]


def get_reddit_posts(company_name: str) -> List[Dict[str, Any]]:
    """Fetch real Reddit posts for a company using PRAW.

    Args:
        company_name (str): The company name to search Reddit posts for.

    Returns:
        List[Dict[str, Any]]: List of Reddit post dictionaries.
    """
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    posts = []
    for submission in reddit.subreddit('all').search(company_name, sort='new', limit=10):
        posts.append({
            "id": submission.id,
            "text": submission.title,
            "author": str(submission.author) if submission.author else None,
            "timestamp": datetime.utcfromtimestamp(submission.created_utc).isoformat(),
            "source": "reddit",
            "company_query": company_name,
        })
    return posts


def get_mock_news_articles(company_name: str) -> List[Dict[str, Any]]:
    """Fetch mock news articles for a company.

    Args:
        company_name (str): The company name to search news articles for.

    Returns:
        List[Dict[str, Any]]: List of mock news article dictionaries.
    """
    return [
        {
            "id": "news_201",
            "text": "Google announces breakthrough in quantum computing.",
            "author": "TechNewsDaily",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "news",
            "company_query": company_name,
        },
        {
            "id": "news_202",
            "text": "MarketWatch: Google's stock rises after strong earnings report.",
            "author": "MarketWatch",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "news",
            "company_query": company_name,
        },
        {
            "id": "news_203",
            "text": "Forbes: Google expands its cloud business with new partnerships.",
            "author": "Forbes",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "news",
            "company_query": company_name,
        },
    ]
