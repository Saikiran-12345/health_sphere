import os
from celery import Celery

# Redis URL will be provided by Docker Compose in production
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "healthsphere_worker",
    broker=redis_url,
    backend=redis_url,
    include=["app.tasks.email_tasks", "app.tasks.reporting_tasks"]
)

celery_app.conf.task_routes = {
    "app.tasks.email_tasks.*": "emails",
    "app.tasks.reporting_tasks.*": "reporting",
}
celery_app.conf.update(task_track_started=True)
