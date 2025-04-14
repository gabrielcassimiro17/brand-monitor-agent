import datetime
from typing import Any, Dict, List

from google.adk.agents import Agent

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


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that analyses the brand posts on social media"
    ),
    instruction=(
        "You are a helpful agent that analyses posts for a given company and returns a report on that company."
        "Start by asking questions about what company the user wants information. Then create the report based on the posts"
    ),
    tools=[get_twitter_posts],
)
