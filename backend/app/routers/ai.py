from fastapi import APIRouter

from app.services.router_service import decide_tool
from app.services.tool_executor import execute_tool

router = APIRouter(
    prefix="/api/ai",
    tags=["AI Agent"],
)


@router.post("/chat")
def chat(payload: dict):
    user_input = payload["message"]

    decision = decide_tool(user_input)

    result = execute_tool(
        decision["tool"],
        decision["arguments"],
    )

    return result