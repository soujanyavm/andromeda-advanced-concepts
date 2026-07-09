from typing import Any, Dict
from andromeda.core.workflow import WorkflowBuilder

def step_one(state: Dict[str, Any]) -> Dict[str, Any]:
    return state | {"messages": state.get("messages", []) + ["first"]}

def step_two(state: Dict[str, Any]) -> Dict[str, Any]:
    return state | {"messages": state.get("messages", []) + ["second"]}

builder = WorkflowBuilder(name="stream_values")
(
    builder.start("first").run(step_one)
    .finish("second").run(step_two)
)

for chunk in builder.stream(state={"messages": []}):
    print(chunk)

# Typical values-mode chunks:
# {"messages": []}
# {"messages": ["first"]}
# {"messages": ["first", "second"]}