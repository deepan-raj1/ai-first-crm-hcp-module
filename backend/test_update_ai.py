from app.services.ai_service import extract_update_data

result = extract_update_data(
    """
Change sentiment to Neutral.

Follow-up after two weeks.

Outcome should be Positive response.
"""
)

print(result)