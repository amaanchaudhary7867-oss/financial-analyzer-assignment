from celery import Celery

# Create Celery instance
celery = Celery(
    "financial_analyzer",

    # Redis is used as message broker (queue)
    broker="redis://localhost:6379/0",

    # Redis is also used to store results
    backend="redis://localhost:6379/0"
)