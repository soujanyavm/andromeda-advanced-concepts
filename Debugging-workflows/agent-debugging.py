from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig
from langchain.messages import HumanMessage

# Debug Level 0: No debugging (default)
config_level_0 = AgentConfig(
    name="normal_agent",
    model=ModelConfig(name="llama3:8b", provider="litellm"),
    debug=0  # No debug output
)

# Debug Level 1: Input/Output logging only
config_level_1 = AgentConfig(
    name="io_debug_agent",
    model=ModelConfig(name="llama3:8b", provider="litellm"),
    debug=1  # Shows input and output messages
)

# Debug Level 2: Full method tracing
config_level_2 = AgentConfig(
    name="trace_agent",
    model=ModelConfig(name="llama3:8b", provider="litellm"),
    debug=2  # Traces all method calls with PyEZTrace
)

# Debug Level 3: Full tracing + LangGraph debugging
config_level_3 = AgentConfig(
    name="full_debug_agent",
    model=ModelConfig(name="llama3:8b", provider="litellm"),
    debug=3  # Maximum debugging with LangGraph internals
)

# Create and use debug agent
debug_agent = Agent(config_level_1)
messages = [HumanMessage(content="Hello, debug me!")]
result = debug_agent.invoke(messages)  # Will show I/O logs