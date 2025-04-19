from pydantic import BaseModel
from typing import List

class TwitterPost(BaseModel):
    id: str
    text: str
    author: str
    timestamp: str
    source: str
    company_query: str

class TwitterPostsResponse(BaseModel):
    twitter_posts: List[TwitterPost]
