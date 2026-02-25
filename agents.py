from crewai import Agent
from tools import read_data_tool

llm = "groq/llama-3.3-70b-versatile"

financial_analyst = Agent(
    role="Senior Financial Analyst",

    goal="""
    Analyze financial documents and provide financial insights,
    risk assessment, and investment recommendations
    """,

    backstory="""
    CFA-certified financial analyst expert in financial report analysis.
    """,

    tools=[read_data_tool],

    verbose=True,

    memory=True,

    llm=llm
)