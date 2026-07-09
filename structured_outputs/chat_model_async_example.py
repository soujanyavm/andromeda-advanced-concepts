import asyncio
from typing import Optional
from pydantic import BaseModel
from andromeda.utils.langtils import get_chat_model
from andromeda import HumanMessage
from andromeda.config import ModelConfig

chat_model = get_chat_model(
    ModelConfig(name="qwen3.5:9b", provider="ollama")
)

class SummaryModel(BaseModel):
    topic: str
    key_points: list[str]
    risk_rating: Optional[str] = None

async def main() -> None:
    structured_llm = chat_model.with_structured_output(SummaryModel)
    out = await structured_llm.ainvoke([
        HumanMessage(content="Summarize AI chip shortage impact in 3 bullets.")
    ])
    print(type(out))
    print(out)
    # Usually a SummaryModel instance

asyncio.run(main())


