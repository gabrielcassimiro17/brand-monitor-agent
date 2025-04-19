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
        "timestamp": (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=2)).isoformat(),
        "source": "twitter",
        "company_query": "Google",
    },
    {
        "id": "tweet_456",
        "text": "Google's latest algorithm update seems to be rolling out. Seeing some ranking changes.",
        "author": "SEOGuru",
        "timestamp": (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1)).isoformat(),
        "source": "twitter",
        "company_query": "Google",
    },
    {
        "id": "tweet_789",
        "text": "Using Google Workspace for collaboration is seamless. Highly recommend!",
        "author": "RemoteWorker",
        "timestamp": (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3)).isoformat(),
        "source": "twitter",
        "company_query": "Google",
    },
]


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

mcp = FastApiMCP(
    app,
    name="Get the company Posts",
    description="Returns social media posts of the given company",
    base_url="http://127.0.0.1:7000",
)
mcp.mount()
