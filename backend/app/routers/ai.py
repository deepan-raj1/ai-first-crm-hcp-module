from fastapi import APIRouter

from app.ai.graph import crm_graph

router = APIRouter(
    prefix="/api/ai",
    tags=["AI Agent"],
)


@router.post("/chat")
def chat(payload: dict):
    state = {
        "user_input": payload["message"],
        "tool_name": None,
        "interaction_data": {},
        "messages": [],
        "response": "",
    }

    result = crm_graph.invoke(state)

    return {
        "response": result["response"]
    }