from google.adk.agents import Agent
from .tools import get_twitter_posts

root_agent = Agent(
    name="brand_monitor_agent",
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
