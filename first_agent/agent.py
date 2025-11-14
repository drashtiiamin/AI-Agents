from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.0-flash',
    name='first_agent',
    description='Greeting Agent',
    instruction="""
    You are a helpful assistant that greets users.
    Ask user for their name and greet them using their name.
    """,
)
