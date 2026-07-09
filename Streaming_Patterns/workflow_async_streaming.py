import asyncio
from typing import Any, Dict
from andromeda.core.workflow import WorkflowBuilder

def step_one(state: Dict[str, Any]) -> Dict[str, Any]:
    return state | {"messages": state.get("messages", []) + ["first"]}

def step_two(state: Dict[str, Any]) -> Dict[str, Any]:
    return state | {"messages": state.get("messages", []) + ["second"]}

async def main() -> None:
    builder = WorkflowBuilder(name="astream_values")
    (
        builder.start("first").run(step_one)
        .finish("second").run(step_two)
    )

    async for chunk in builder.astream(state={"messages": []}):
        print(chunk)

asyncio.run(main())