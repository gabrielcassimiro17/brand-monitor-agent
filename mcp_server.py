import datetime
from typing import Any, Dict, List

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


def get_twitter_posts(company_name: str) -> dict:
    """Returns posts for the company name

    Args:
        company_name (str): The name of the company to search posts on social media

    Returns:
        dict: status and result or error msg.
    """

    if company_name.lower() == "google":
         report = (
            f'The posts for {company_name}: {MOCK_GOOGLE_POSTS}'
        )

    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {company_name}."
            ),
        }

    return {"status": "success", "report": report}
