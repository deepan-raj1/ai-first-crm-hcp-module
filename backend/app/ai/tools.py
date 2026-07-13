from langchain_core.tools import tool

from app.database.connection import SessionLocal
from app.schemas.interaction import (InteractionCreate, InteractionUpdate,)
from app.services.ai_service import (
    extract_interaction,
    normalize_interaction_data,
    extract_update_data,
    summarize_text,
)
from app.services.interaction_service import (create_interaction, update_interaction, get_interactions_by_hcp,)


@tool
def log_interaction(user_input: str):
    """
    Extract CRM interaction details using AI
    and save them into PostgreSQL.
    """

    data = extract_interaction(user_input)

    data = normalize_interaction_data(data)

    db = SessionLocal()

    try:
        interaction = InteractionCreate(**data)

        saved = create_interaction(db, interaction)

        return {
            "status": "success",
            "id": saved.id,
            "hcp_name": saved.hcp_name,
            "message": "Interaction saved successfully.",
            "interaction": data,
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        db.close()


@tool
def edit_interaction(interaction_id: int, user_input: str):
    """
    Update an existing interaction using AI.
    """

    data = extract_update_data(user_input)

    db = SessionLocal()

    try:
        interaction = update_interaction(
            db,
            interaction_id,
            InteractionUpdate(**data)
        )

        if not interaction:
            return {
                "status": "error",
                "message": "Interaction not found."
            }

        return {
            "status": "success",
            "id": interaction.id,
            "message": "Interaction updated successfully.",
            "updated_fields": data
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        db.close()

@tool
def get_interaction_history(hcp_name: str):
    """
    Retrieve interaction history for a Healthcare Professional.
    """

    db = SessionLocal()

    try:
        interactions = get_interactions_by_hcp(db, hcp_name)

        if not interactions:
            return {
                "status": "error",
                "message": f"No interactions found for {hcp_name}."
            }

        result = []

        for interaction in interactions:
            result.append({
                "id": interaction.id,
                "hcp_name": interaction.hcp_name,
                "interaction_type": interaction.interaction_type,
                "date": str(interaction.date),
                "summary": interaction.summary,
                "sentiment": interaction.sentiment,
            })

        return {
            "status": "success",
            "count": len(result),
            "interactions": result,
        }

    finally:
        db.close()

@tool
def summarize_interaction(interaction_text: str):
    """
    Generate a professional CRM summary.
    """

    summary = summarize_text(interaction_text)

    return {
        "status": "success",
        "summary": summary,
    }

@tool
def recommend_follow_up(summary: str) -> str:
    """
    Recommend next best action.
    """
    return (
        "Recommended follow-up: "
        "Schedule another visit within two weeks."
    )