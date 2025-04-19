from typing import List, Dict, Any
import datetime

# Mock repositories for each source

def get_mock_twitter_posts(company_name: str) -> List[Dict[str, Any]]:
    return [
        {
            "id": "tweet_123",
            "text": "Excited about the new features announced at Google I/O! #GoogleIO #AI",
            "author": "TechEnthusiast",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "twitter",
            "company_query": company_name
        },
        {
            "id": "tweet_456",
            "text": "Google's latest algorithm update seems to be rolling out. Seeing some ranking changes.",
            "author": "SEOGuru",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "twitter",
            "company_query": company_name
        },
        {
            "id": "tweet_789",
            "text": "Using Google Workspace for collaboration is seamless. Highly recommend!",
            "author": "RemoteWorker",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "twitter",
            "company_query": company_name
        }
    ]

def get_mock_reddit_posts(company_name: str) -> List[Dict[str, Any]]:
    return [
        {
            "id": "reddit_101",
            "text": "Redditors discuss Google's latest AI advancements in r/technology.",
            "author": "RedditTechie",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "reddit",
            "company_query": company_name
        },
        {
            "id": "reddit_102",
            "text": "AMA with a Google engineer happening now in r/IAmA!",
            "author": "AskMeAnything",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "reddit",
            "company_query": company_name
        },
        {
            "id": "reddit_103",
            "text": "Reddit users share their experience with Google Pixel devices.",
            "author": "PixelFan",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "reddit",
            "company_query": company_name
        }
    ]

def get_mock_news_articles(company_name: str) -> List[Dict[str, Any]]:
    return [
        {
            "id": "news_201",
            "text": "Google announces breakthrough in quantum computing.",
            "author": "TechNewsDaily",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "news",
            "company_query": company_name
        },
        {
            "id": "news_202",
            "text": "MarketWatch: Google's stock rises after strong earnings report.",
            "author": "MarketWatch",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "news",
            "company_query": company_name
        },
        {
            "id": "news_203",
            "text": "Forbes: Google expands its cloud business with new partnerships.",
            "author": "Forbes",
            "timestamp": datetime.datetime.now().isoformat(),
            "source": "news",
            "company_query": company_name
        }
    ]
