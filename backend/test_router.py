from app.services.router_service import decide_tool

result = decide_tool(
    "Log today's visit with Dr Rahul. Discussed CardioMax and gave 5 sample packs."
)

print(result)