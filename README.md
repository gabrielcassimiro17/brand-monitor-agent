# Brand Monitor Agent

Brand Monitor Agent is an agent-based system built with Google ADK to analyze a company's brand presence across social media (Twitter, Reddit) and news articles. The agent uses a Model Context Protocol (MCP) server, implemented with FastAPI, as a set of tools to fetch brand-related data. The MCP server exposes endpoints for retrieving data, which the agent leverages to generate comprehensive brand reports.

## Features
- **Agent Orchestration**: Uses Google ADK to run a multi-step workflow that fetches and analyzes content from all sources and compiles a brand report.
- **MCP Server (FastAPI)**: Provides REST API endpoints (`/twitter`, `/reddit`, `/news`) that serve as tools for the agent, returning mock data for a given company.

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/gabrielcassimiro17/brand-monitor-agent.git
cd brand-monitor-agent/brand-monitor
```

### 2. Set up your environment variables
Create a `.env` file at the root of the `brand-monitor` directory. The most important variable is your Google API key:

```bash
echo "GOOGLE_API_KEY=your-google-api-key" > .env
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" >> .env
```

Or copy and edit the provided example:
```bash
cp .env.example .env
```

---

## Running the MCP Server

Start the FastAPI MCP server on port 7000:

```bash
uvicorn brand-monitor.mcp.mcp_server:app --port 7000
```

The MCP endpoints will be available at [http://127.0.0.1:7000](http://127.0.0.1:7000).

---

## Using the Agent with ADK Web

To launch the agent's interactive web UI (using Google ADK):

```bash
adk web
```

This will open a browser window where you can interact with the Brand Monitor Agent, select a company, and generate a brand report.

---

## .env Example
See `.env.example` for required environment variables.

---

## Project Structure
- `mcp/` - FastAPI MCP server, routers, services, repositories, schemas
- `brand_monitor_agent/` - Agent logic, tools, and agent orchestration

---

## License
MIT License
