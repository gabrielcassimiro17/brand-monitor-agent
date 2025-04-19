from google.adk.agents import LlmAgent
from ..tools import get_posts

news_agent = LlmAgent(
    name="NewsFetcher",
    model="gemini-2.0-flash",
    description="Analyze recent news articles for the target company.",
    instruction=(
        "Use the get_posts tool with source='news' and company=state['company'] to fetch the 5 latest articles. "
        "Then write a concise report summarizing the headlines, overall tone, and any emerging news trends or key developments."
    ),
    tools=[get_posts],
    output_key="news_report",
)
