from google.adk.agents import ParallelAgent, SequentialAgent
from .agents.twitter_agent import twitter_agent
from .agents.reddit_agent import reddit_agent
from .agents.news_agent import news_agent
from .agents.compile_agent import compile_agent

# Fan-out to run each analysis in parallel
parallel_fetch = ParallelAgent(
    name="FetchParallel",
    sub_agents=[twitter_agent, reddit_agent, news_agent],
)

# Orchestrator
brand_monitor_workflow = SequentialAgent(
    name="BrandMonitorWorkflow",
    sub_agents=[
        parallel_fetch,
        compile_agent,
    ],
)

# Root agent reference for the runner
root_agent = brand_monitor_workflow
