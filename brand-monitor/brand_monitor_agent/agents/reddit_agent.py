"""Reddit Agent module.

Returns:
    LlmAgent: Agent that analyzes recent Reddit discussions for the target company.
"""

from google.adk.agents import LlmAgent
from ..tools import get_posts


def create_reddit_agent() -> LlmAgent:
    """Creates an agent to analyze recent Reddit discussions for the target company.

    Args:
        None

    Returns:
        LlmAgent: Configured Reddit analysis agent.
    """
    return LlmAgent(
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


reddit_agent = create_reddit_agent()
