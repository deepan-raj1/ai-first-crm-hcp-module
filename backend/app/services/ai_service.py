import json
import os
from datetime import datetime

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)


def extract_interaction(user_input: str) -> dict:
    """
    Extract structured interaction details from natural language
    using the Groq LLM.
    """

    prompt = f"""
You are an AI assistant for a Pharmaceutical CRM.

Extract the following fields from the interaction.

Return ONLY valid JSON.

Rules:

- topics_discussed must be a string.
- attendees must be a string.
- materials_shared must be a string.
- samples_distributed must be a string
  (Example: "10 Sample Packs", "Brochure Shared", "None").

- sentiment should be one of:
  Positive
  Neutral
  Negative

- interaction_type should be one of:
  Clinic Visit
  Phone Call
  Video Meeting
  Conference
  Follow-up

- If date is not mentioned, use today's date.
- If time is not mentioned, use the current time.

Fields:

hcp_name
interaction_type
date
time
attendees
topics_discussed
materials_shared
samples_distributed
sentiment
outcome
follow_up_actions
summary

User Input:

{user_input}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove Markdown code block if present
    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    return json.loads(content)


def normalize_interaction_data(data: dict) -> dict:
    """
    Convert AI output into the format expected by
    the InteractionCreate schema.
    """

    now = datetime.now()

    # Fill missing date/time
    if not data.get("date"):
        data["date"] = now.date().isoformat()

    if not data.get("time"):
        data["time"] = now.strftime("%H:%M:%S")

    # Convert list -> string
    if isinstance(data.get("topics_discussed"), list):
        data["topics_discussed"] = ", ".join(
            data["topics_discussed"]
        )

    # Convert boolean -> string
    if isinstance(data.get("samples_distributed"), bool):
        data["samples_distributed"] = (
            "Yes" if data["samples_distributed"] else "No"
        )

    # Fill missing optional fields
    optional_fields = [
        "attendees",
        "materials_shared",
        "samples_distributed",
        "sentiment",
        "outcome",
        "follow_up_actions",
        "summary",
        "topics_discussed",
    ]

    for field in optional_fields:
        if data.get(field) is None:
            data[field] = ""

    return data


def extract_update_data(user_input: str) -> dict:
    """
    Extract only the fields that need updating.
    """

    prompt = f"""
You are an AI assistant for a Pharmaceutical CRM.

The user wants to UPDATE an existing interaction.

Return ONLY valid JSON.

Return ONLY the fields that the user wants to modify.

Use ONLY the following field names:

hcp_name
interaction_type
date
time
attendees
topics_discussed
materials_shared
samples_distributed
sentiment
outcome
follow_up_actions
summary

Do NOT invent new field names.
Do NOT include fields that are not being updated.

Example:

User:
Change sentiment to Neutral.
Follow-up after two weeks.

Output:
{{
    "sentiment": "Neutral",
    "follow_up_actions": "Follow-up after two weeks"
}}

User:

{user_input}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    return json.loads(content)


def summarize_text(interaction_text: str) -> str:
    """
    Generate a professional CRM summary.
    """

    prompt = f"""
You are an AI assistant for a Pharmaceutical CRM.

Summarize the following interaction into a concise professional CRM note.

Keep it between 40 and 80 words.

Interaction:

{interaction_text}
"""

    response = llm.invoke(prompt)

    return response.content.strip()


def recommend_next_action(summary: str) -> str:
    """
    Recommend the next best follow-up action.
    """

    prompt = f"""
You are an AI assistant for a Pharmaceutical CRM.

Based on the interaction summary below, recommend the next best action for the sales representative.

Rules:
- Keep the recommendation practical.
- Limit it to 2–3 sentences.
- Focus on strengthening the relationship with the HCP.

Interaction Summary:

{summary}
"""

    response = llm.invoke(prompt)

    return response.content.strip()

