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

## Setup Instructions

Step 1: Clone repository

git clone https://github.com/amaanchaudhary7867-oss/financial-analyzer-assignment.git

cd financial-analyzer-assignment  

Step 2: Create virtual environment

python -m venv venv  

Activate:

Windows:
venv\Scripts\activate  

Step 3: Install dependencies

pip install -r requirements.txt  

Step 4: Add environment variable

Create .env file:

GROQ_API_KEY=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  

Step 5: Start Redis

redis-server  

Step 6: Start Celery worker

celery -A worker worker --loglevel=info --pool=solo  

Step 7: Start FastAPI

uvicorn main:app --reload  

Open browser:

http://127.0.0.1:8000/docs

---

## Bugs Found and Fixes 

### Bug 1: Redis connection error 
Error: ``` Could not create server TCP listening socket ``` 
Fix: Started Redis server manually using: ``` redis-server ```
--- 

### Bug 2: Tool validation error in CrewAI 
Error: ``` Input should be instance of BaseTool ``` 
Fix: Converted tool function into CrewAI Tool class. 
--- 

### Bug 3: Celery worker import error 
Error: ``` Unable to load celery application ``` 
Fix: Corrected module imports and verified worker.py location. 
--- 

### Bug 4: Output truncation in Celery Fix: 
Modified worker task to print full result instead of returning truncated response. 

---Installation Instructions

Step 1: Clone repository

git clone https://github.com/amaanchaudhary7867-oss/financial-analyzer.git 

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

GROQ_API_KEY=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

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

- Multiple documents can be processed simultaneously

- FastAPI remains responsive

- Background processing improves scalability

- Production-ready architecture

- Redis acts as message broker between FastAPI and Celery worker.

- Celery worker continuously listens for new tasks.

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

---
## Screenshots

## Screenshots Included screenshots showing:
- FastAPI Swagger interface
- Celery worker running
- Redis server running
- Task processing output
- Financial analysis report generated

Screenshots located in: ``` screenshots/ ```

### API Documentation (FastAPI Swagger)
![API Docs]
<img width="1920" height="1080" alt="api_docs" src="https://github.com/user-attachments/assets/03deb4df-0102-4c41-b876-659d5ae238a5" />

### Celery Worker Processing Task
![Celery Worker]
<img width="1920" height="1080" alt="celery_worker (2)" src="https://github.com/user-attachments/assets/785fa361-b00a-4c1c-bc10-7f360638ce06" />
<img width="1920" height="1080" alt="celery_worker (1)" src="https://github.com/user-attachments/assets/59c810bf-f6dd-48c6-8651-a3f132cc7e40" />
<img width="1920" height="1080" alt="celery_worker (4)" src="https://github.com/user-attachments/assets/5bc6fc6b-a5d5-41c0-b7dc-8f09ad661d47" />
<img width="1920" height="1080" alt="celery_worker (3)" src="https://github.com/user-attachments/assets/4752d769-324f-4396-86f1-be635f823447" />

### Financial Analysis Output
![Analysis Output]
<img width="1920" height="1080" alt="api_execution" src="https://github.com/user-attachments/assets/6198973d-34ed-4215-b407-7060fb9b07d7" />

### Project Structure in VS Code
![Project Structure]
<img width="224" height="403" alt="project_structure" src="https://github.com/user-attachments/assets/3a1123f6-beeb-4498-ac01-e77c3e6bff5e" />

---
## Status

Assignment Requirements Completed
Requirement	Status
CrewAI agent	Completed
Tool integration	Completed
FastAPI backend	Completed
Celery queue worker	Completed
Redis integration	Completed
Async processing	Completed
Financial analysis	Completed

---

Author 

Amaan Chaudhary
Mumbai, India
+91 76780-94773
Gmail: amaanchaudhary7867@gmail.com
GitHub: https://github.com/amaanchaudhary7867-oss/financial-analyzer-assignment

---

## Conclusion 

This project successfully implements a scalable financial document analysis system using AI and asynchronous processing. The system meets all assignment requirements and demonstrates integration of FastAPI, CrewAI, Groq LLM, Celery, and Redis.
