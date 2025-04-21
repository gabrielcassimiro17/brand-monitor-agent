from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from .routers import router

app = FastAPI()
app.include_router(router)

mcp = FastApiMCP(
    app,
    name="Get the company Posts",
    description="Returns social media posts and news articles of the given company",
)
mcp.mount()
