# Brand Monitor Agent

Brand Monitor Agent is an agent-based system built with Google ADK to analyze a company's brand presence across social media (Twitter, Reddit) and news articles. The agent uses a Model Context Protocol (MCP) server, implemented with FastAPI, as a set of tools to fetch, process, and synthesize brand-related data. The MCP server exposes endpoints for retrieving mock data, which the agent leverages to generate comprehensive brand reports.

This project is under development. For now you can run it locally.

## Architecture

### MCP Server

The MCP server is a FastAPI application using the MCP protocol that provides REST API endpoints for fetching mock data from Twitter, Reddit, and news articles. This service is deployed on cloud run.

### Agent

The agent is a Google ADK-based system that uses the MCP server as a set of tools to fetch, process, and synthesize brand-related data. This service is deployed on cloud run using de ADK SDK.

### Front End

The front end is a web interface that allows users to interact with the agent and generate brand reports.

The front end will be build with firebase studio.


## Features
- **Agent Orchestration**: Uses Google ADK to run a multi-step workflow that fetches and analyzes content from all sources and compiles a brand report.
- **MCP Server (FastAPI)**: Provides REST API endpoints (`/twitter`, `/reddit`, `/news`) that serve as tools for the agent, returning data for a given company.

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/gabrielcassimiro17/brand-monitor-agent.git
cd brand-monitor
```

### 2. Set up your environment variables
Create a `.env` file at the root of the `brand-monitor` directory. The most important variable is your Google API key:

```bash
echo "GOOGLE_API_KEY=your-google-api-key" > .env
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" >> .env
```

See `.env.example` for required environment variables.

Or copy and edit the provided example:
```bash
cp .env.example .env
```

#### Reddit API Credentials
To enable live Reddit search, add these to your `.env`:
```env
REDDIT_CLIENT_ID=your-reddit-client-id
REDDIT_CLIENT_SECRET=your-reddit-client-secret
REDDIT_USER_AGENT=brand-monitor-agent
```

---

## Local Development Setup

Before running the MCP server, set up your Python environment:

```bash
# Create and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r mcp/requirements.txt
```

---

## Running the MCP Server (Docker)

Start the FastAPI MCP server using Docker:

```bash
cd mcp
# Build the Docker image
docker build -t mcp-server .
# Run the Docker container
docker run --env-file ../.env -p 7001:7001 mcp-server
```

The MCP endpoints will be available at [http://127.0.0.1:7001](http://127.0.0.1:7001).

---

## Using the Agent with ADK Web

To launch the agent's interactive web UI (using Google ADK):

```bash
adk web
```

This will open a browser window where you can interact with the Brand Monitor Agent, select a company, and generate a brand report.
---

## Project Structure
- `mcp/` - FastAPI app, routers, services, repositories, schemas
- `brand_monitor_agent/` - Agent logic, tools, and agent orchestration

---

## License
MIT License
