from celery_config import celery

from crewai import Crew, Process

from agents import financial_analyst

from task import analyze_financial_document

from database import save_result


@celery.task
def analyze_task(file_path, query, filename):

    # Create Crew
    crew = Crew(

        agents=[financial_analyst],

        tasks=[analyze_financial_document],

        process=Process.sequential
    )

    result = crew.kickoff(inputs={"file_path": file_path})

    print("\n\nFULL RESULT:\n")
    print(result)

    # Save result in database
    save_result(filename, query, str(result))