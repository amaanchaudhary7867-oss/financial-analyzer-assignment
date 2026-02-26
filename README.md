# Financial Document Analyzer using CrewAI, FastAPI, Celery, and Redis

## Assignment Submission Repository:
https://github.com/amaanchaudhary7867-oss/financial-analyzer-assignment

## Overview

This project implements an AI-powered Financial Document Analyzer that reads financial PDF documents and generates a structured financial analysis report.

The system uses CrewAI agents, Groq LLM, FastAPI, Celery, and Redis to process documents asynchronously and provide investment insights including revenue trends, profitability, cash flow analysis, risks, and recommendations.

The architecture follows a production-style design with API backend, background workers, and AI agents.

---

## System Architecture

Components:

- FastAPI → handles file uploads and API requests
- Celery → handles background task processing
- Redis → message broker between FastAPI and Celery
- CrewAI Agent → performs financial analysis
- Groq LLM → provides AI reasoning
- Tool → reads financial PDF document

Workflow:

1. User uploads financial document via FastAPI
2. FastAPI saves file locally
3. FastAPI sends task to Celery queue
4. Celery worker receives task
5. CrewAI agent reads document using tool
6. Agent analyzes financial data using Groq LLM
7. Agent generates structured financial analysis report
8. Result returned to user

---

## Technologies Used

- Python 3.11
- FastAPI
- CrewAI
- Celery
- Redis
- Groq LLM (llama-3.3-70b-versatile)
- LiteLLM
- PyPDF
- Uvicorn

---

## Bugs Found and Fixes

### Bug 1: Tool validation error

Error:


ValidationError: tools.0 Input should be a valid dictionary or BaseTool


Cause:

CrewAI expects tools to be defined using the `@tool` decorator, not plain functions.

Fix:

Updated tools.py:

Before:

```python
def read_data_tool(file_path):

After:

from crewai.tools import tool

@tool("Financial Document Reader")
def read_data_tool(file_path: str) -> str:
Bug 2: Celery output truncation

Problem:

Celery was truncating output because return value was too large.

Fix:

Removed return statement and used print():

Before:

return result

After:

print(result)
Bug 3: Agent calling tool multiple times

Problem:

Agent repeatedly called the tool unnecessarily.

Fix:

Improved task instructions:

Use the Financial Document Reader tool ONLY ONCE.
After reading, DO NOT use any tool again.
Installation Instructions
Step 1: Clone repository
git clone https://github.com/yourusername/financial-analyzer.git
cd financial-analyzer
Step 2: Create virtual environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate
Step 3: Install dependencies
pip install -r requirements.txt
Step 4: Start Redis server
redis-server
Step 5: Configure environment variables

Create .env file:

GROQ_API_KEY=your_groq_api_key
Step 6: Start FastAPI server
uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs
Step 7: Start Celery worker

Open new terminal:

celery -A worker worker --loglevel=info --pool=solo
API Documentation
Endpoint: Upload Financial Document

POST /analyze

Description:

Uploads financial document and triggers analysis.

Request:

Multipart form-data:

file: PDF document

Response:

{
    "task_id": "uuid"
}
Celery Worker

Celery worker receives task:

worker.analyze_task

Processes document asynchronously.

Example Output

Generated report includes:

Revenue Performance

Profitability Analysis

Cash Flow Analysis

Financial Risks

Investment Recommendation

Example recommendation:

Recommendation: HOLD
Reason: Declining revenue but strong liquidity position
Queue Worker Model Implementation (Bonus Requirement)

This project uses Celery with Redis to support asynchronous and concurrent processing.

Advantages:

Multiple documents can be processed simultaneously

FastAPI remains responsive

Background processing improves scalability

Production-ready architecture

Redis acts as message broker between FastAPI and Celery worker.

Celery worker continuously listens for new tasks.

Project Structure
financial-analyzer/

main.py        → FastAPI backend
worker.py      → Celery worker
agents.py      → CrewAI agent definition
task.py        → Task definition
tools.py       → Financial document reader tool
requirements.txt
README.md
data/
How to Use

Start Redis

Start Celery worker

Start FastAPI server

Open:

http://127.0.0.1:8000/docs

Upload financial document

Check Celery terminal for output

Assignment Requirements Completed
Requirement	Status
CrewAI agent	Completed
Tool integration	Completed
FastAPI backend	Completed
Celery queue worker	Completed
Redis integration	Completed
Async processing	Completed
Financial analysis	Completed
Author

Amaan Chaudhary
Mumbai, India
+91 76780-94773
Gmail: amaanchaudhary7867@gmail.com
