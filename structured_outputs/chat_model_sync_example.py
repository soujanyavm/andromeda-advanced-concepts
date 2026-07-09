from typing import TypedDict, Optional
from andromeda import HumanMessage
from andromeda.utils.langtils import get_chat_model
from andromeda.config import ModelConfig

chat_model = get_chat_model(
    ModelConfig(name="qwen3.5:9b", provider="ollama")
)

class SummaryTD(TypedDict):
    topic: str
    key_points: list[str]
    risk_rating: Optional[str]

structured_llm = chat_model.with_structured_output(SummaryTD, method="json_schema")
out = structured_llm.invoke([
    HumanMessage(content="Summarize AI chip shortage impact for cloud providers.")
])
print(type(out))
print(out)
# Usually a dict matching SummaryTD

