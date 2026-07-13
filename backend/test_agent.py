from app.services.router_service import decide_tool
from app.services.tool_executor import execute_tool

user_input = "Visited Dr. Rahul today, discussed CardioMax and gave 5 sample packs."

decision = decide_tool(user_input)

print("Router Decision:")
print(decision)

print()

result = execute_tool(
    decision["tool"],
    decision["arguments"],
)

print("Tool Result:")
print(result)