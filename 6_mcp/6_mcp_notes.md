## 6_mcp_notes

### MCP = Model Context Protocol
- What it's not
  - A framework for building agents
  - A fundamental change to how agents work
  - A way to code agents
- What it is
  - A protocol - a standard
  - A simple way to integrate tools, resources, prompts
  - "A USB-C port for AI applications"
- Reasons not to be excited
  - It's just a standard, it's not the tools themselves
  - LangChain already has a big Tools ecosystem
  - You can already make any function into a Tool
- Reasons to be excited
  - Makes it frictionless to integrate with others' tools
  - It's taking off! Exploding ecosystem
  - HTML was just a standard too

### MCP Core Concepts
- Main components
  - Host: LLM app like Claude or our Agent architecture
  - MCP Client: lives inside the host and connects 1:1 to MCP Server
  - MCP Server: provides tools, context and prompts
- Example
  - Fetcher is an MCP Server that searches the web via a headless browser
  - You can configure Claude Desktop (the host) to run an MCP Client that then launches the Fetcher MCP Server on your computer

### Architecture
- Download open-source MCP Servers, run them locally
- Two "Transport" mechanisms
  - Stio spawns a process and communicates via standard input/output
  - while SSE uses HTTPS connections with streaming

### Making an MCP Server
- Why make an MCP Server?
  - Allow others to incorporate tools and resources
  - Consistently incorporate all our MCP Servers
  - Understand the plumbing
- Reasons not to
  - If it's only for us, then we could just make tools - the @function_tool decorator can make any function into a tool
- MCP is all about sharing tools and resources with others

### Which framework to select?
- It's not the most important question and it doesn't really matter!
- Pick the framework that suits your style and the skills of your team

### What matters
1. Start with the problem, not the solution
2. Have a metric to evaluate success
3. Favor workflow over autonomy initially
4. Work bottom up, not top down
5. Start simple, then add
6. Start with large frontier models, then reduce
7. Think context rather than memory
8. Most problems are solved with better prompts
9. Look at the traces
10. Be a scientist; no shortcut to R&D