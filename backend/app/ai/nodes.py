import os

from langchain_groq import ChatGroq

from app.ai.state import AgentState
from app.ai.prompts import SYSTEM_PROMPT
from app.ai.tools import (
    log_interaction,
    edit_interaction,
    get_interaction_history,
    summarize_interaction,
    recommend_follow_up,
)

from dotenv import load_dotenv
load_dotenv()

tools = [
    log_interaction,
    edit_interaction,
    get_interaction_history,
    summarize_interaction,
    recommend_follow_up,
]

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
)

llm_with_tools = llm.bind_tools(tools)

def assistant_node(state: AgentState):
    """
    Main AI assistant node.
    """

    user_input = state["user_input"]

    prompt = f"""
{SYSTEM_PROMPT}

User:
{user_input}
"""

    response = llm_with_tools.invoke(prompt)

    state["llm_response"] = response

    print("========== RESPONSE ==========")
    print(response)
    print("==============================")

    state["response"] = response.content

    return state



def execute_tool_node(state: AgentState):
    """
    Execute the tool requested by the LLM.
    """

    response = state["llm_response"]

    if not response.tool_calls:
        return state

    tool_call = response.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    tool_map = {
        "log_interaction": log_interaction,
        "edit_interaction": edit_interaction,
        "get_interaction_history": get_interaction_history,
        "summarize_interaction": summarize_interaction,
        "recommend_follow_up": recommend_follow_up,
    }

    tool = tool_map[tool_name]

    result = tool.invoke(tool_args)

    state["response"] = result

    return state