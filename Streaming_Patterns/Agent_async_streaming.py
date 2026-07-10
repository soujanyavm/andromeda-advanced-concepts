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

    async for chunk in agent.astream(history, stream_mode="values", remember="last"):
        print(chunk)

asyncio.run(main())