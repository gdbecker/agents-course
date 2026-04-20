## 3_crewai_notes

### CrewAI has several offerings
- CrewAI Enterprise
  - A multi-agent platform for deploying, running and monitoring Agentic AI
- CrewAI UI Studio
  - A no-code/low-code product for creating multi-agent solutions
- CrewAI open-source framework
  - "Orchestrate high performing AI agents with ease and scale"

### The framework comes in two flavors
- CrewAI Crews
  - Autonomous solutions with AI teams of Agents with different roles
  - "Choose Crews when: you need autonomous problem-solving, creative collaboration or exploratory tasks" 
- CrewAI Flows
  - Structured automations by dividing complex tasks into precise workflows
  - "Choose Flows when: you require deterministic outcomes, auditability, or precise control over execution"

### Core Concepts
- Agent: an autonomous unit, with an LLM, a role, a goal, a backstory, memory, and tools
- Task: a specific assignment to be carried out, with a description, expected output, and agent
- Crew: a team of Agents and Tasks
  - either Sequential: run in order they are defined 
  - or Hierarchical: use a Manager LLM to assign

### YAML Configuration
- Agents and Tasks can be created by code, setting the backstory, description, expected output, etc
- Or you can define each in a YAML file that's provided when you create the code
  - Lightweight and nice separation of things you need

### crew.py
- It all comes together with a Crew definition

### LLMs
- CrewAI uses the super-simple LiteLLM under the hood to interface with almost any LLM; set keys in the .env file

### CrewAI projects are UV projects
- CrewAI is already installed: `uv tool install crewai`
- Make a new project: `crewai create crew my_crew`
- This creates an entire directory structure