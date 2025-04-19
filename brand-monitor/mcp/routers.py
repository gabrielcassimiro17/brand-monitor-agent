from fastapi import APIRouter, Query
from .services import fetch_twitter_posts, fetch_reddit_posts, fetch_news_articles
from .schemas import TwitterPostsResponse

router = APIRouter()

@router.get("/twitter", operation_id="get_twitter_posts", response_model=TwitterPostsResponse)
async def get_twitter_posts(company_name: str = Query(..., description="Company name to search tweets for")):
    return fetch_twitter_posts(company_name)

@router.get("/reddit", operation_id="get_reddit_posts", response_model=TwitterPostsResponse)
async def get_reddit_posts(company_name: str = Query(..., description="Company name to search reddit posts for")):
    return fetch_reddit_posts(company_name)

@router.get("/news", operation_id="get_news_articles", response_model=TwitterPostsResponse)
async def get_news_articles(company_name: str = Query(..., description="Company name to search news articles for")):
    return fetch_news_articles(company_name)
