from crewai import Task
from agents import financial_analyst

analyze_financial_document = Task(
    description="""
    Step 1:
    Use the Financial Document Reader tool ONLY ONCE to read the financial document at {file_path}.

    Step 2:
    After reading the document, DO NOT use any tool again.
    Analyze the financial data and prepare a detailed financial analysis.

    Include:

    1. Revenue Performance
       - Total revenue trend
       - Growth or decline %
       - Segment performance

    2. Profitability Analysis
       - Net income
       - Operating income
       - Profit margins
       - EBITDA trends

    3. Cash Flow Analysis
       - Operating cash flow
       - Free cash flow
       - Capital expenditures
       - Liquidity position

    4. Financial Risks
       - Declining revenue or margins
       - Increasing expenses
       - Cash flow risks
       - Operational risks

    5. Investment Recommendation
       - Strong Buy, Buy, Hold, or Sell
       - Justify with financial reasoning

    Step 3:
    Provide the FINAL ANSWER directly as a professional financial analyst report.
    Do NOT attempt to use any tool after reading the document.
    """,

    expected_output="""
    A complete professional financial analysis report including:

    - Revenue Analysis
    - Profitability Analysis
    - Cash Flow Analysis
    - Financial Risks
    - Investment Recommendation

    With clear reasoning and final conclusion.
    """,

    agent=financial_analyst
)