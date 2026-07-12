from langgraph.graph import StateGraph, START, END

from app.ai.state import AgentState
from app.ai.nodes import assistant_node

# Create graph
builder = StateGraph(AgentState)

# Add nodes
builder.add_node("assistant", assistant_node)

# Define flow
builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)

# Compile graph
crm_graph = builder.compile()