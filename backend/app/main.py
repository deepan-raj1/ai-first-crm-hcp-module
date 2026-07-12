from fastapi import FastAPI

from app.database.connection import engine
from app.database.base import Base
from app.routers.interaction import router as interaction_router


# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-First CRM HCP Module API",
    description="Backend API for AI-First CRM using FastAPI, LangGraph and Groq",
    version="1.0.0"
)

app.include_router(interaction_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI-First CRM HCP Module API 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

