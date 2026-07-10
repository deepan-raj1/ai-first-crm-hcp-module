from fastapi import FastAPI

app = FastAPI(
    title="AI-First CRM HCP Module API",
    description="Backend API for AI-First CRM using FastAPI, LangGraph and Groq",
    version="1.0.0"
)


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