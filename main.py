from fastapi import FastAPI, UploadFile, File, Form

import os
import uuid

from worker import analyze_task


app = FastAPI(title="Financial Analyzer API")


@app.get("/")
def home():

    return {"status": "API running"}


@app.post("/analyze")
async def analyze(

        file: UploadFile = File(...),

        query: str = Form("Analyze financial document")

):

    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    # Save uploaded file
    file_id = str(uuid.uuid4())

    file_path = f"data/{file_id}.pdf"


    with open(file_path, "wb") as f:

        content = await file.read()

        f.write(content)


    # Send task to Celery worker
    task = analyze_task.delay(

        file_path,

        query,

        file.filename
    )


    return {

        "task_id": task.id,

        "status": "processing"
    }