from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams


# Update MCPToolset to use the correct /mcp endpoint as per fastapi_mcp documentation
async def get_posts(company_name: str, source: str, **kwargs) -> str:
    """
    Asynchronously fetches posts or articles for the given company name and source using the MCP toolset.

    Args:
        company_name (str): The name of the company to search.
        source (str): The source to search ('twitter', 'reddit', or 'news').

    Returns:
        str: The result of the tool execution as a string.
    """
    tx = kwargs.get("tx")
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(url="http://127.0.0.1:7001/mcp")
    )
    async with exit_stack:
        # Find the tool by name
        tool = next(
            t
            for t in tools
            if t.name == f"get_{source}_posts" or t.name == f"get_{source}_articles"
        )
        return await tool.run_async(
            args={"company_name": company_name}, tool_context=tx
        )
