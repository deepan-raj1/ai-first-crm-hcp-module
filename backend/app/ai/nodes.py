import os

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="gemma2-9b-it",
    api_key=os.getenv("GROQ_API_KEY"),
)