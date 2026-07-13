from app.ai.tools import get_interaction_history

result = get_interaction_history.invoke(
    {
        "hcp_name": "Sarah"
    }
)

print(result)