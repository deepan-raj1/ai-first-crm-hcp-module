from langchain_core.tools import tool

from app.services.ai_service import extract_interaction


@tool
def log_interaction(user_input: str) -> dict:
    """
    Extract structured CRM interaction details from natural language.
    """

    data = extract_interaction(user_input)

    return data

@tool
def edit_interaction(interaction_id: int, updated_data: str) -> str:
    """
    Edit an existing interaction.
    """
    return f"Interaction {interaction_id} updated."


@tool
def get_interaction_history(hcp_name: str) -> str:
    """
    Retrieve interaction history for an HCP.
    """
    return f"Retrieved interaction history for {hcp_name}."


@tool
def summarize_interaction(interaction_text: str) -> str:
    """
    Generate a professional summary.
    """
    return f"Summary: {interaction_text}"


@tool
def recommend_follow_up(summary: str) -> str:
    """
    Recommend next best action.
    """
    return (
        "Recommended follow-up: "
        "Schedule another visit within two weeks."
    )