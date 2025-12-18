from google.adk.agents import LlmAgent
from google.adk.tools import google_search

finance_assistant_agent = LlmAgent(
    name="FinanceAssistant",
    model="gemini-2.5-flash",
   description="""
You are FinanceAssistant, an AI agent specialized in financial advice.

You help users with:
- Budgeting
- Investment strategies
- Financial planning

Always ensure advice is safe, conservative, and based on sound financial principles.
""",
tools=[google_search]
)


root_agent=finance_assistant_agent