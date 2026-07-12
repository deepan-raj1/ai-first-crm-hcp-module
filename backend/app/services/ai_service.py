import json
from urllib import response
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
)


def extract_interaction(user_input: str):
    prompt = f"""
Extract the following fields from the CRM interaction.

Return ONLY valid JSON.

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

    # response = llm.invoke(prompt)

    # print("========== LLM RESPONSE ==========")
    # print(response.content)
    # print("==================================")

    # return response.content

    response = llm.invoke(prompt)

    content = response.content.strip()

    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    return json.loads(content)