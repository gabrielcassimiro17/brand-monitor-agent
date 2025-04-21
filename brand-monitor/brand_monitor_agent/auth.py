import os
from google.auth.transport.requests import Request
from google.oauth2 import id_token

# Utility to fetch a Google Cloud identity token for Cloud Run auth

def get_id_token(audience: str = None) -> str:
    """
    Fetches an identity token for the given Cloud Run service URL.
    If audience is not provided, uses MCP_REMOTE_URL from env (without /mcp).
    """
    if audience is None:
        url = os.getenv("MCP_REMOTE_URL", "").rstrip("/mcp")
        audience = url
    return id_token.fetch_id_token(Request(), audience)
