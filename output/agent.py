from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

#Define Output schema for email agent
class EmailOutput(BaseModel):
    subject: str = Field(..., description="The subject of the email")
    body: str = Field(..., description="The body content of the email")
    recipient: str = Field(..., description="The recipient's email address")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='output_agent',
    description='A helpful assistant for user email drafting needs.',
    instruction="""
    -create an email draft based on user requests with proper subject line.
    - write well-structured email body. with proper greetings and sign-offs.
    - ensure clarity and conciseness in the email content.  
    - Email tone should match the user's intent (formal/informal).
    - provide the recipient's email address if specified by the user.
    Instructions: Your response must strictly adhere to the output schema provided.
    {
        "subject": "Subject of the email",
        "body": "Body content of the email",
        "recipient": "Recipient's email address"
    }
    - do not include any additional text outside the JSON structure.
    """,
    output_schema=EmailOutput,
    output_key="email_draft",
)