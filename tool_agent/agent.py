from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
    from datetime import datetime
    now = datetime.now()
    return {"current_time": now.strftime("%Y-%m-%d %H:%M:%S"),}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='tool_agent',
    description='Tool Agent',
    instruction="""
    You are a helpful assistant that uses the following tools to assist users:
    - get current time
    """,
    #tools=[google_search], # built-in tool example
    tools=[get_current_time], # custom tool example
) 
