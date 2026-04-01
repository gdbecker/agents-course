import gradio as gr

def create_app():
    with gr.Blocks(title="Master AI Agentic Engineering") as demo:
        gr.Markdown("""
# Master AI Agentic Engineering
### Build autonomous AI Agents with OpenAI Agents SDK, CrewAI, LangGraph, AutoGen and MCP

---

Welcome to the **6-week journey** into Agentic AI! This repository contains all the course labs, notebooks, and projects.

## Course Structure

| Week | Topic | Key Tools |
|------|-------|-----------|
| **Week 1** | Foundations | OpenAI, Gradio, Tool Calling |
| **Week 2** | OpenAI Agents SDK | Deep Research, Agents SDK |
| **Week 3** | CrewAI | Multi-Agent Systems, CrewAI |
| **Week 4** | LangGraph | Agent Orchestration, LangGraph |
| **Week 5** | AutoGen | Multi-Agent Conversations |
| **Week 6** | MCP | Model Context Protocol |

## Getting Started

1. **Set your API keys** — create a `.env` file with your `OPENAI_API_KEY` and other keys as needed
2. **Run a notebook** — open any `*.ipynb` file in the weekly folders
3. **Run an app** — navigate to the week's folder and run the `app.py` (e.g. `python 1_foundations/app.py`)

## Key Resources

- **Guides** — foundational notebooks in the `guides/` folder
- **Setup instructions** — in the `setup/` folder for Windows, Mac, and Linux
- **Community contributions** — found in each week's `community_contributions/` folder

---

*Created by Edward Donner — [LinkedIn](https://www.linkedin.com/in/eddonner/) | [Course Resources](https://edwarddonner.com/2025/04/21/the-complete-agentic-ai-engineering-course/)*
        """)

    return demo


if __name__ == "__main__":
    app = create_app()
    app.launch(server_name="0.0.0.0", server_port=5000)
