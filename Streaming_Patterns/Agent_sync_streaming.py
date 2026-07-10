from andromeda import HumanMessage
from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig

agent = Agent(
    AgentConfig(
        name="streamer_sync",
        model=ModelConfig(name="qwen3.5:9b", provider="ollama"),
    )
)

history = [HumanMessage(content="Explain streaming in simple terms.")]

for chunk in agent.stream(history, stream_mode="values", remember="all"):
    print(chunk)