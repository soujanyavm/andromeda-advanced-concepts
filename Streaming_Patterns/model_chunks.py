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
    
    async for event in agent.astream(history, stream_mode="events"):
        if event.get("event") == "on_chat_model_stream":
            chunk = event.get("data", {}).get("chunk")
            print(chunk, end="")
asyncio.run(main())