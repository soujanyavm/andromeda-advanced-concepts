import asyncio
from andromeda import HumanMessage
from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig

async def main() -> None:
    
    agent = Agent(
        AgentConfig(
            name="streamer_async",
            model=ModelConfig(name="qwen3.5:9b", provider="ollama"),
        )
    )
    history = [HumanMessage(content="Explain Andromeda in streaming mode.")]
    
    async for ev in agent.astream_structured_events(history):
        if ev["type"] == "response_chunk":
            print(ev["content"], end="", flush=True)
        elif ev["type"] == "tool_call":
            print(f"\n[tool] {ev['raw']['name']}")
        elif ev["type"] == "tool_result":
            print(f"\n[tool done] {ev['raw']['name']}")
        elif ev["type"] == "response_end":
            print("\n--- done ---")

asyncio.run(main())