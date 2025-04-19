from google.adk.agents import Agent
from .tools import get_posts

root_agent = Agent(
    name="brand_monitor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that analyses the brand posts on social media (Twitter, Reddit) and news articles."
    ),
    instruction=(
        "You are a helpful agent that analyses posts and news articles for a given company and returns a report on that company. "
        "Start by asking questions about what company the user wants information. "
        "Then create the report based on the posts and articles you find. "
        "You can fetch posts from Twitter, Reddit, or news articles individually. "
        "Ask the user which sources they want to include."
    ),
    tools=[get_posts],
)
