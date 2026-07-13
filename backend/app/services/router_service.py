import json

from app.services.ai_service import llm


def decide_tool(user_input: str) -> dict:
    """
    Decide which tool should handle the user's request.
    Return ONLY valid JSON.
    """

    prompt = f"""
You are an AI router for a Pharmaceutical CRM.

Choose exactly ONE tool.

Available tools:

1. log_interaction
2. edit_interaction
3. get_interaction_history
4. summarize_interaction
5. recommend_follow_up

Return ONLY JSON.

Example:

{{
    "tool": "log_interaction",
    "arguments": {{
        "user_input": "Visited Dr. Rahul today..."
    }}
}}

User:

{user_input}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    return json.loads(content.strip())