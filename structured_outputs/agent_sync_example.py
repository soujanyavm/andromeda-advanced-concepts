from typing import Optional, TypedDict
from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig
from andromeda import HumanMessage
from pydantic import BaseModel

class RiskBrief(BaseModel):
    topic: str
    key_points: list[str]
    risk_rating: Optional[str]

cfg = AgentConfig(
    name="structured_agent_sync",
    model=ModelConfig(name="qwen3.5:9b", provider="ollama"),
    response_format=RiskBrief,
    prompt="Always return the requested schema.",
)

agent = Agent(cfg)
messages = [
    HumanMessage(content="Summarize risks of AI chip shortages for cloud providers.")
]

out = agent.invoke(messages)
print(type(out))
print(out)
# Example shape:
# {
#   "topic": "AI chip shortages for cloud providers",
#   "key_points": ["...", "..."],
#   "risk_rating": "medium"
# }

