from google.adk.agents import LlmAgent
from ..tools import get_posts

twitter_agent = LlmAgent(
    name="TwitterFetcher",
    model="gemini-2.0-flash",
    description="Analyze recent tweets for the target company.",
    instruction=(
        "Use the get_posts tool with source='twitter' and company=state['company'] to fetch the 5 most recent tweets. "
        "Then write a concise report highlighting the main themes, overall sentiment, and any key influencers or popular hashtags."
    ),
    tools=[get_posts],
    output_key="twitter_report",
)
