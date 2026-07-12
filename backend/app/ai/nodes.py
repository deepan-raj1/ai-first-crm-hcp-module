import os

from langchain_groq import ChatGroq

from app.ai.state import AgentState
from app.ai.prompts import SYSTEM_PROMPT

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
)


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

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state