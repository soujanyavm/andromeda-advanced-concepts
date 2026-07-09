import asyncio
from typing import Optional
from pydantic import BaseModel
from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig
from andromeda import HumanMessage

class RiskBriefModel(BaseModel):
    topic: str
    key_points: list[str]
    risk_rating: Optional[str] = None

async def main() -> None:
    cfg = AgentConfig(
        name="structured_agent_async",
        model=ModelConfig(name="qwen3.5:9b", provider="ollama"),
        response_format=RiskBriefModel,
        prompt="Return output that matches RiskBriefModel.",
    )

    agent = Agent(cfg)
    out = await agent.ainvoke([
        HumanMessage(content="Summarize AI chip supply-chain risk in 3 points.")
    ])
    print(type(out))
    print(out)
    # Often a RiskBriefModel instance:
    # RiskBriefModel(topic="...", key_points=[...], risk_rating="...")

asyncio.run(main())