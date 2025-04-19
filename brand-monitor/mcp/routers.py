"""API Routers for MCP endpoints.

Returns:
    FastAPI APIRouter: Router containing endpoints for Twitter, Reddit, and News.
"""

from fastapi import APIRouter, Query
from .services import fetch_twitter_posts, fetch_reddit_posts, fetch_news_articles
from .schemas import TwitterPostsResponse, RedditPostsResponse, NewsArticlesResponse

router = APIRouter()


@router.get(
    "/twitter", operation_id="get_twitter_posts", response_model=TwitterPostsResponse
)
async def get_twitter_posts(
    company_name: str = Query(..., description="Company name to search tweets for")
) -> dict:
    """Endpoint to retrieve Twitter posts for a specified company.

    Args:
        company_name (str): The company name to search tweets for.

    Returns:
        dict: Dictionary containing a list of Twitter posts for the company.
    """
    return fetch_twitter_posts(company_name)


@router.get(
    "/reddit", operation_id="get_reddit_posts", response_model=RedditPostsResponse
)
async def get_reddit_posts(
    company_name: str = Query(
        ..., description="Company name to search reddit posts for"
    )
) -> dict:
    """Endpoint to retrieve Reddit posts for a specified company.

    Args:
        company_name (str): The company name to search Reddit posts for.

    Returns:
        dict: Dictionary containing a list of Reddit posts for the company.
    """
    return fetch_reddit_posts(company_name)


@router.get(
    "/news", operation_id="get_news_articles", response_model=NewsArticlesResponse
)
async def get_news_articles(
    company_name: str = Query(
        ..., description="Company name to search news articles for"
    )
) -> dict:
    """Endpoint to retrieve news articles for a specified company.

    Args:
        company_name (str): The company name to search news articles for.

    Returns:
        dict: Dictionary containing a list of news articles for the company.
    """
    return fetch_news_articles(company_name)
