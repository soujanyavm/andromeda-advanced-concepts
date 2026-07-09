from typing import Any, Dict
from andromeda.core.workflow import Command, WorkflowBase
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
initial = WorkflowBase.run(builder, state={"messages": []})
# ... approval or external signal occurs ...
resumed = builder.stream(
    resume=Command(goto="second"),
    thread_id=initial.context.thread_id,
)
for chunk in resumed:
    print(chunk)