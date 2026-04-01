# Master AI Agentic Engineering

## Project Overview
A 6-week course repository for building autonomous AI Agents. Created by Edward Donner. Covers OpenAI Agents SDK, CrewAI, LangGraph, AutoGen, and MCP (Model Context Protocol).

## Architecture
- **Language:** Python 3.12
- **Package Manager:** `uv` (with `pyproject.toml` and `uv.lock`)
- **UI Framework:** Gradio (for interactive demos)
- **Entry Point:** `app.py` — a Gradio landing page that documents the course structure

## Course Structure
- `1_foundations/` — Foundational labs (OpenAI, Tool Calling, Gradio)
- `2_openai/` — OpenAI Agents SDK, Deep Research
- `3_crew/` — CrewAI multi-agent systems
- `4_langgraph/` — LangGraph agent orchestration
- `5_autogen/` — AutoGen multi-agent conversations
- `6_mcp/` — Model Context Protocol
- `guides/` — Foundational Jupyter notebooks
- `setup/` — Platform-specific setup instructions

## Running the App
The main workflow runs JupyterLab on port 5000, serving the entire workspace so all course notebooks are accessible in the browser. Individual week labs also have their own `app.py` files that can be run separately via the terminal.

JupyterLab is configured to:
- Bind to `0.0.0.0:5000` for Replit's proxy
- Disable token/password for dev access
- Allow all origins (`allow_origin=*`) for the iframe proxy

## Environment Variables
Users need to create a `.env` file with:
- `OPENAI_API_KEY` — required for most labs
- `ANTHROPIC_API_KEY` — optional, for Anthropic models
- `LANGCHAIN_API_KEY` / `LANGSMITH_API_KEY` — optional, for LangSmith tracing
- Other keys as needed per lab (Polygon, SendGrid, Pushover, etc.)

## Key Dependencies
- `openai`, `openai-agents` — OpenAI SDK and Agents SDK
- `anthropic` — Anthropic Claude models
- `crewai` — CrewAI framework (install separately via `uv tool install crewai==0.130.0 --python 3.12`)
- `langgraph`, `langchain-openai`, `langchain-anthropic` — LangGraph / LangChain
- `autogen-agentchat`, `autogen-ext` — AutoGen framework
- `mcp` — Model Context Protocol
- `gradio` — Web UI for demos
- `playwright` — Web scraping

## Workflow
- **Start application** — `python app.py` on port 5000 (webview)
