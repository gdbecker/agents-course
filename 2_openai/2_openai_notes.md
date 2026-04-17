## 2_openai_notes

### asyncio package
- All the Agent frameworks use asynchronous Python
- The short version
  - All your methods and functions start with "async"
  - Anytime you call them. use "await"
- The long version
  - Asyncio provides a lightweight alternative to threading or multiprocessing
  - Functions defined with async def are called coroutines - they're special functions that can be paused and resumed
  - Calling a coroutine doesn't execute immediately - it returns a coroutine object
  - To actually run a coroutine, you must await it, which schedules it for execution within an event loop
  - While a coroutine is waiting (like for I/O), the event loop can run other coroutines
  - It's a manual way of handling multi-threading
  - Easy and quick to get running

### OpenAI Agents SDK
- Features
  - Lightweight and flexible
  - Stays out of the way
  - Makes common activities easy
  - Ed's favorite
- Minimal terminology
  - Agents represent LLMs
  - Handoffs represent interactions
  - Guardrails represent controls
- Three steps
  - Create an instance of Agent
  - Use "with trace()" to track the agent
  - Call "runner.run()" to run the agent

### Vibe Coding Tips
- Good vibes - prompt well - ask for short answers and latest APIs for today's date
  - Mention today's date
- Vibe but verify - ask 2 LLMs the same question
- Step up the vibe - ask to break down your request into independently testable steps
- Vibe and validate - ask an LLM then get another LLM to check
- Vibe with variety - ask for 3 solutions to the same problem, pick the best