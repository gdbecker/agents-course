## 5_autogen_notes

### AutoGen (AG)
- AutoGen 0.4 released January 2025
  - from the ground up rewrite adopting an asynchronous, event-driven architecture to address issues such as observability, flexibility, interactive control and scale
  - Complete replacement for AutoGen 0.2
- AutoGen Core
  - Event-driven framework for scalable multi-agent AI systems
- AutoGent AgentChat
  - Conversational Single and Multi-Agent Applications
- Studio
  - Low-Code / No-Code app
- Magnetic One CLI
  - A console-based assistant

### AutoGen DRAMA
- Several of the original developers of AutoGen left Microsoft and split off in late 2024 to create a fork of AutoGen
- Called AG2 or AgentOS 2, compatible with earlier AutoGen 0.2
- If you pip install autogen, you get AG2!

### AutoGen Core Concepts
- Models
- Messages
- Agents
- Teams

### AutoGen Core
- An Agent interaction framework
- Agnostic to Agent abstraction
- Somewhat similar positioning to LangGraph
- But focus is on managing interactions between distributed and diverse Agents
- Fundamental principle
  - Decouples an Agent's logic from how messages are delivered
  - The framework handles creation and communication
  - The Agents are responsible for their logic - that is not the remit of AutoGen Core
- Two types of runtime
  - Standalone
  - Distributed
    - Handles lifecycle and communication across process boundaries, consisting of
      - A host service, connected to worker runtimes, handling message delivery and sessions for direct messages
      - A worker runtime, advertises agents to the host service and handles executing their code

### This week's ending project
- Explore the dynamic nature of AutoGen
- Make a "Creator" agent that can write a Python module
- The Python module is an Agent: An AutoGen AgentChat Agent in AutoGen Core
- Then have the Creator agent actually register its creation with a distributed runtime
- Have it make creations that can message each other by their names
- Make them collaborate to come up with a commercial business idea for Agents