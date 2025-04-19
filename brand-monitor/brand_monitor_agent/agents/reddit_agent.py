from google.adk.agents import LlmAgent
from ..tools import get_posts

reddit_agent = LlmAgent(
    name="RedditFetcher",
    model="gemini-2.0-flash",
    description="Analyze recent Reddit discussions for the target company.",
    instruction=(
        "Use the get_posts tool with source='reddit' and company=state['company'] to fetch the top 5 posts. "
        "Then write a concise report summarizing the primary discussion topics, community sentiment, and notable user insights."
    ),
    tools=[get_posts],
    output_key="reddit_report",
)
