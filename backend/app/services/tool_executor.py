from app.ai.tools import (
    log_interaction,
    edit_interaction,
    get_interaction_history,
    summarize_interaction,
    recommend_follow_up,
)

TOOL_MAP = {
    "log_interaction": log_interaction,
    "edit_interaction": edit_interaction,
    "get_interaction_history": get_interaction_history,
    "summarize_interaction": summarize_interaction,
    "recommend_follow_up": recommend_follow_up,
}


def execute_tool(tool_name: str, arguments: dict):
    """
    Execute the selected tool.
    """

    tool = TOOL_MAP.get(tool_name)

    if tool is None:
        return {
            "status": "error",
            "message": f"Unknown tool: {tool_name}",
        }

    return tool.invoke(arguments)