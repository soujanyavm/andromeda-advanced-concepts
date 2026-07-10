from andromeda.core.agent import Agent
from andromeda.config import AgentState, AgentConfig, ModelConfig, MiddlewareConfig

class CustomAgentState(AgentState):
    user_id: str

cfg = AgentConfig(
    name="assistant_with_state",
    model=ModelConfig(name="llama3.1:8b", provider="litellm"),
    state_schema=CustomAgentState,
    middleware=MiddlewareConfig(
        tool_error_handler=True,
        summarization=MiddlewareConfig.SummarizationOptions(
            trigger_tokens=1200,
        ),
        guardrails=MiddlewareConfig.GuardrailOptions(
            input=True,
            output=True,
            tool=False,
        ),
    ),
)
agent = Agent(cfg)