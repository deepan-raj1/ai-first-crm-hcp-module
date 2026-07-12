from app.ai.tools import log_interaction

result = log_interaction.invoke(
    {
        "user_input": "Visited Dr. John today. Discussed CardioMax. Doctor requested samples."
    }
)

print(result)