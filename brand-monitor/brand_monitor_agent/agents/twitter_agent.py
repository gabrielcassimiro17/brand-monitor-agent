"""Twitter Agent module.

Returns:
    LlmAgent: Agent that analyzes recent tweets for the target company.
"""
from google.adk.agents import LlmAgent
from ..tools import get_posts

def create_twitter_agent() -> LlmAgent:
    """Creates an agent to analyze recent tweets for the target company.

    Args:
        None

    Returns:
        LlmAgent: Configured Twitter analysis agent.
    """
    return LlmAgent(
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

twitter_agent = create_twitter_agent()
