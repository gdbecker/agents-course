## 4_langgraph_notes

### The LangChain ecosystem
- **LangChain** is an open source framework with a pre-built agent architecture and integrations for any model or tool, so you can build agents that adapt as fast as the ecosystem evolves.
  - LangChain is the easy way to start building completely custom agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and more. LangChain provides a prebuilt agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications.
  - LangChain agents are built on top of LangGraph in order to provide durable execution, streaming, human-in-the-loop, persistence, and more. You do not need to know LangGraph for basic LangChain agent usage.
- Trusted by companies shaping the future of agents— including Klarna, Uber, J.P. Morgan, and more— **LangGraph** is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.
  - LangGraph is very low-level, and focused entirely on agent orchestration. Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with models and tools.
- LangChain vs. LangGraph vs. Deep Agents
  - If you are looking to build an agent, we recommend you start with Deep Agents which comes “batteries-included”, with modern features like automatic compression of long conversations, a virtual filesystem, and subagent-spawning for managing and isolating context.
  - Deep Agents are implementations of LangChain agents. If you don’t need these capabilities or would like to customize your own for your agents and autonomous applications, start with LangChain.
  - Use LangGraph, our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows and heavy customization.
- LangGraph is 3 things:
  - LangGraph (focusing on this during the course)
  - LangGraph Studio
  - LangGraph Platform

### Terminology
- Agent Workflows are represented as graphs
- State represents the current snapshot of the application
- Nodes are python functions that represent agent logic
  - They receive the current State as input, do something, and return the updated State
- Edges are python functions that determine which Node to execute nex based on the State
  - They can be conditional or fixed
- Nodes to the work
- Edges choose what to do next

### 5 steps to the first Graph
1. Define the State class
2. Start the Graph Builder
3. Create a Node
4. Create Edges
5. Compile the Graph

More on the State
- State is immutable
- For each field in your State, you can specify a special function called a reducer
- When you return a new State, LangGraph uses the reducer to combine this field with existing State
- This enables LangGraph to run multiple nodes concurrently and combine State without overwriting

The Super-Step
- Can be considered a single iteration over the graph nodes. Nodes that run in parallel are part of the same Super-Step, while nodes that run sequentially belong to separate Super-Steps
- The graph describes one Super-Step
  - One interaction between agents and tools to achieve an outcome
- Every user interaction is a fresh graph.invoke(state) call
- The reducer handles updating state during a Super-Step but not between Super-Steps

Bringing it together
1. Define the Graph
2. Super-Step (graph is invoked)
3. Super-Step (graph is invoked)
4. Super-Step (graph is invoked)
- Need to add checkpointing in between each Super-Step