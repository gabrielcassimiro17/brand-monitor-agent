import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, Query
from fastapi_mcp import FastApiMCP
from .schemas import TwitterPost, TwitterPostsResponse

MOCK_GOOGLE_POSTS: List[Dict[str, Any]] = [
    {
        "id": "tweet_123",
        "text": "Excited about the new features announced at Google I/O! #GoogleIO #AI",
        "author": "TechEnthusiast",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "twitter",
        "company_query": "Google"
    },
    {
        "id": "tweet_456",
        "text": "Google's latest algorithm update seems to be rolling out. Seeing some ranking changes.",
        "author": "SEOGuru",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "twitter",
        "company_query": "Google"
    },
    {
        "id": "tweet_789",
        "text": "Using Google Workspace for collaboration is seamless. Highly recommend!",
        "author": "RemoteWorker",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "twitter",
        "company_query": "Google"
    }
]

MOCK_REDDIT_POSTS = [
    {
        "id": "reddit_101",
        "text": "Redditors discuss Google's latest AI advancements in r/technology.",
        "author": "RedditTechie",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "reddit",
        "company_query": "Google"
    },
    {
        "id": "reddit_102",
        "text": "AMA with a Google engineer happening now in r/IAmA!",
        "author": "AskMeAnything",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "reddit",
        "company_query": "Google"
    },
    {
        "id": "reddit_103",
        "text": "Reddit users share their experience with Google Pixel devices.",
        "author": "PixelFan",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "reddit",
        "company_query": "Google"
    }
]

MOCK_NEWS_ARTICLES = [
    {
        "id": "news_201",
        "text": "Google announces breakthrough in quantum computing.",
        "author": "TechNewsDaily",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "news",
        "company_query": "Google"
    },
    {
        "id": "news_202",
        "text": "MarketWatch: Google's stock rises after strong earnings report.",
        "author": "MarketWatch",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "news",
        "company_query": "Google"
    },
    {
        "id": "news_203",
        "text": "Forbes: Google expands its cloud business with new partnerships.",
        "author": "Forbes",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "news",
        "company_query": "Google"
    }
]

## Todo:
# add integration to twitter
# add integration to reddit
# add integration to tavily

app = FastAPI()


@app.get("/twitter", operation_id="get_twitter_posts", response_model=TwitterPostsResponse)
async def get_twitter_posts(company_name: str = Query(..., description="Company name to search tweets for")):
    """
    Endpoint to retrieve Twitter posts for a specified company.

    Args:
        company_name (str): The name of the company to search tweets for (as a query parameter).

    Returns:
        dict: Dictionary containing a list of Twitter posts for the company.
    """
    return {"twitter_posts": MOCK_GOOGLE_POSTS}

@app.get("/reddit", operation_id="get_reddit_posts", response_model=TwitterPostsResponse)
async def get_reddit_posts(company_name: str = Query(..., description="Company name to search reddit posts for")):
    """
    Mock endpoint to retrieve Reddit posts for a specified company.
    """
    return {"twitter_posts": MOCK_REDDIT_POSTS}

@app.get("/news", operation_id="get_news_articles", response_model=TwitterPostsResponse)
async def get_news_articles(company_name: str = Query(..., description="Company name to search news articles for")):
    """
    Mock endpoint to retrieve news articles for a specified company.
    """
    return {"twitter_posts": MOCK_NEWS_ARTICLES}

mcp = FastApiMCP(
    app,
    name="Get the company Posts",
    description="Returns social media posts and news articles of the given company",
    base_url="http://127.0.0.1:7000",
)
mcp.mount()
