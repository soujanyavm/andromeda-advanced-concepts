import asyncio
from andromeda.core.agent import Agent
from andromeda.config import AgentConfig, ModelConfig
from andromeda import HumanMessage
async def main() -> None:
    agent = Agent(
        AgentConfig(
            name="streamer_async",
            model=ModelConfig(name="qwen3.5:9b", provider="ollama"),
        )
    )
    history = [HumanMessage(content="Explain Andromeda in streaming mode.")]
    async for event in agent.astream(history, stream_mode="events"):
        etype = event.get("event")
    if etype == "on_chat_model_stream":
        print("model chunk", event.get("data", {}))
    elif etype == "on_tool_start":
        print("tool start", event.get("name"))
    elif etype == "on_tool_end":
        print("tool end", event.get("name"))
asyncio.run(main())