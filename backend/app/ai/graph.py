from langgraph.graph import StateGraph, START, END

from app.ai.state import AgentState
from app.ai.nodes import (
    assistant_node,
    execute_tool_node,
)


def should_use_tool(state: AgentState):
    """
    Decide whether to execute a tool or finish.
    """

    response = state["llm_response"]

    if response.tool_calls:
        return "tool"

    return "end"


# Create graph
builder = StateGraph(AgentState)

# Add nodes
builder.add_node("assistant", assistant_node)
builder.add_node("tool", execute_tool_node)

# Start
builder.add_edge(START, "assistant")

# Conditional routing
builder.add_conditional_edges(
    "assistant",
    should_use_tool,
    {
        "tool": "tool",
        "end": END,
    },
)

# Finish
builder.add_edge("tool", END)

# Compile
crm_graph = builder.compile()