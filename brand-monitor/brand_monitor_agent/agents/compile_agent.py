"""Compile Agent module.

Returns:
    LlmAgent: Agent that combines all source-specific analyses into one brand report.
"""
from google.adk.agents import LlmAgent

def create_compile_agent() -> LlmAgent:
    """Creates an agent to compile all source-specific analyses into a brand report.

    Args:
        None

    Returns:
        LlmAgent: Configured brand report compilation agent.
    """
    return LlmAgent(
        name="ReportCompiler",
        model="gemini-2.0-flash",
        description="Combine all source-specific analyses into one cohesive brand report.",
        instruction=(
            "You have three inputs in state: 'twitter_report', 'reddit_report', and 'news_report'. "
            "Compile these into a single, structured brand monitoring report that includes an executive summary and key takeaways from each source."
            "Return the report in markdown format."
        ),
        output_key="final_report",
    )

compile_agent = create_compile_agent()
