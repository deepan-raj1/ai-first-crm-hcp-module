from typing import TypedDict, Optional, List, Dict, Any


class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    """

    # User input
    user_input: str

    # Tool selected by the AI
    tool_name: Optional[str]

    # Extracted interaction data
    interaction_data: Dict[str, Any]

    # Conversation history
    messages: List[Dict[str, str]]

    # Final response
    response: str

    llm_response: Any