from app.ai.tools import summarize_interaction

result = summarize_interaction.invoke(
    {
        "interaction_text": """
Visited Dr. Sarah Lee.
Discussed CardioMax benefits.
Shared product brochure.
Doctor requested 10 sample packs.
Agreed to follow up next week.
"""
    }
)

print(result)