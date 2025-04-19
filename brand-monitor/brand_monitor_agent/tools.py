from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams

# Update MCPToolset to use the correct /mcp endpoint as per fastapi_mcp documentation
async def get_twitter_posts(company_name: str, **kwargs) -> str:
    """
    Asynchronously fetches Twitter posts for the given company name using the MCP toolset.

    Args:
        company_name (str): The name of the company to search posts on social media.

    Returns:
        str: The result of the tool execution as a string.
    """
    tx = kwargs.get("tx")
    tools, exit_stack = await MCPToolset.from_server(connection_params=SseServerParams(url='http://127.0.0.1:7000/mcp'))
    async with exit_stack:
        # Find the tool by name
        tool = next(t for t in tools if t.name == 'get_twitter_posts')
        return await tool.run_async(args={"company_name": company_name}, tool_context=tx)