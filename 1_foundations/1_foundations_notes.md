## 1_foundations_notes

### Ambiguity on what Agents actually are
- AI Agents are programs where LLM outputs control the workflow
- In practice, describes an AI solution that involves any or all of these:
  - Multiple LLM calls
  - LLMs with ability to use Tools
  - An environment where LLMs interact
  - A Planner to coordinate activities
  - Autonomy

## Agentic Systems
- Anthropic distinguishes two types:
  - Workflows are systems where LLMs and tools are orchestrated through predefined code paths
  - Agents are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks

## 5 Workflow Design Patterns
1. Prompt Chaining
   1. Decompose into fixed sub-tasks
   2. Frame each LLM call specifically and exactly
2. Routing
   1. Direct an input into a specialized sub-task, ensuring separation of concerns
3. Parallelization
   1. Breaking down tasks and running multiple subtasks concurrently
   2. Code does the orchestration
4. Orchestrator-Worker
   1. Complex tasks are broken down dynamically and combined
   2. The LLM does the orchestration, not the code
5. Evaluator-Optimizer
   1. LLM output is validated by another

## By contrast, Agents
1. Open-ended
2. Feedback loops
3. No fixed path

## Risks of Agent Frameworks
1. Unpredictable path
2. Unpredictable output
3. Unpredictable costs
4. Monitor
5. "Guardrails ensure your agents behave safely, consistently, and within your intended boundaries"

## Agentic AI Frameworks
- Highest complexity
  - LangGraph
  - AutoGen
- Medium complexity
  - OpenAI Agents SDK
  - Crew AI
- Lowest complexity
  - No framework
  - MCP (a protocol, not a framework)
- The one you pick depends on your use case and your preference

## Resources
- Ways to get more out of your agents
- We can provide an LLM with resources to improve its expertise
- This means shoving data relevant to the question into the prompt
- There are techniques like RAG to get really smart at picking relevant content

## "Tools" give LLMs autonomy
- Give an LLM the power to carry out actions like querying a database or messaging other LLMs