from app.ai.tools import edit_interaction

result = edit_interaction.invoke(
    {
        "interaction_id": 3,
        "user_input": """
Change sentiment to Neutral.

Outcome should be Positive response.

Follow-up after two weeks.
"""
    }
)

print(result)