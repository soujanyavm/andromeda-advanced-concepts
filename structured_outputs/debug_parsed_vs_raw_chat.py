from andromeda.utils.langtils import get_chat_model
from andromeda.config import ModelConfig
from typing import TypedDict, Optional
from andromeda import HumanMessage

class SummaryTD(TypedDict):
    topic: str
    key_points: list[str]
    risk_rating: Optional[str]

chat_model = get_chat_model(
    ModelConfig(name="qwen3.5:9b", provider="ollama")
)
debug_out = chat_model.with_structured_output(
    SummaryTD,
    method="json_schema",
    include_raw=True,
).invoke([HumanMessage(content="Summarize in schema format")])

print(debug_out.keys())
# dict_keys(["raw", "parsed", "parsing_error"])
print(debug_out["parsed"])