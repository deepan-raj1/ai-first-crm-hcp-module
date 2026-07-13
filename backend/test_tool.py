from app.ai.tools import log_interaction

result = log_interaction.invoke(
    {
        "user_input": """
Visited Dr. Sarah Lee today.

Discussed CardioMax.

Shared product brochure.

Doctor requested 10 sample packs.

Follow-up next week.
"""
    }
)

print(result)