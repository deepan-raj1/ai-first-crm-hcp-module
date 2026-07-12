from app.services.ai_service import extract_interaction

text = """
Visited Dr. John today.
Discussed CardioMax.
Doctor requested samples.
"""

print(extract_interaction(text))