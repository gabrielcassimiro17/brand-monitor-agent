from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams
import os
from dotenv import load_dotenv, find_dotenv
from .auth import get_id_token

load_dotenv(find_dotenv())

# Use a remote MCP URL (from env or hardcoded for production)
MCP_REMOTE_URL = os.getenv("MCP_REMOTE_URL", None)
print(20*"*")
print(MCP_REMOTE_URL)
print(20*"*")

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
    headers = None
    if MCP_REMOTE_URL:
        # Add Bearer token for Cloud Run auth
        token = get_id_token(MCP_REMOTE_URL.rstrip("/mcp"))
        print(20*"*")
        print(token)
        print(20*"*")
        headers = {"Authorization": f"Bearer {token}"}
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(url=MCP_REMOTE_URL, headers=headers)
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
