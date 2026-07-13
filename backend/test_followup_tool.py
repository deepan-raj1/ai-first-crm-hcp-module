from app.ai.tools import recommend_follow_up

result = recommend_follow_up.invoke(
    {
        "summary": """
Met with Dr. Sarah Lee, discussed CardioMax benefits, shared a product brochure, and provided 10 sample packs. The doctor expressed interest and agreed to continue the discussion next week.
"""
    }
)

print(result)