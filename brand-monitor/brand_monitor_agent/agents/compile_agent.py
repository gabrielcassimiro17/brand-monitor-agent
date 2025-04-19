from google.adk.agents import LlmAgent

compile_agent = LlmAgent(
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
