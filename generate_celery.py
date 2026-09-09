import os
import yaml

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Update Requirements
path_req = "backend/requirements.txt"
with open(path_req, "a") as f:
    f.write("\ncelery\nredis\n")

# 2. Celery Configuration
create_file('backend/app/core/celery_app.py', """
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
""")

# 3. Define Celery Tasks
create_file('backend/app/tasks/email_tasks.py', """
import time
from app.core.celery_app import celery_app

@celery_app.task(name="send_invoice_email")
def send_invoice_email(invoice_id: str, patient_email: str):
    \"\"\"
    Simulates sending an invoice PDF via email synchronously in the background.
    \"\"\"
    # In a real app, this would use smtplib or SendGrid API
    print(f"[CELERY] Preparing to send invoice {invoice_id} to {patient_email}...")
    time.sleep(2)  # Simulate network latency
    print(f"[CELERY] Successfully dispatched invoice email to {patient_email}.")
    return {"status": "success", "invoice_id": invoice_id}
""")

create_file('backend/app/tasks/reporting_tasks.py', """
import time
from app.core.celery_app import celery_app

@celery_app.task(name="generate_monthly_financial_report")
def generate_monthly_financial_report():
    \"\"\"
    Simulates a heavy pandas aggregation task running via Celery Beat.
    \"\"\"
    print("[CELERY] Starting heavy financial aggregation...")
    time.sleep(5)  # Simulate massive DB querying and PDF writing
    print("[CELERY] Financial report generated and saved to S3.")
    return True
""")

# 4. Trigger Task from existing API
path_api = "backend/app/api/payments.py"
with open(path_api, "r") as f:
    content = f.read()

if "from app.tasks.email_tasks import send_invoice_email" not in content:
    content = content.replace(
        "from app.services.pdf_generator import InvoicePDFGenerator",
        "from app.services.pdf_generator import InvoicePDFGenerator\nfrom app.tasks.email_tasks import send_invoice_email"
    )
    # Inside the webhook, trigger the celery task
    webhook_target = "print(f\"Payment success for invoice {session.client_reference_id}\")"
    celery_trigger = webhook_target + "\n        send_invoice_email.delay(session.client_reference_id, 'patient@example.com')"
    content = content.replace(webhook_target, celery_trigger)
    
    with open(path_api, "w") as f:
        f.write(content)

# 5. Update Docker Compose to include Redis and Celery Worker
path_docker = "docker-compose.yml"
with open(path_docker, "r") as f:
    # Very basic string replace to inject Redis and Celery
    docker_content = f.read()

if "redis:" not in docker_content:
    injection = """
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
      
  celery_worker:
    build: 
      context: ./backend
      dockerfile: Dockerfile
    command: celery -A app.core.celery_app worker --loglevel=info -Q emails,reporting
    environment:
      - REDIS_URL=redis://redis:6379/0
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/healthsphere
    depends_on:
      - redis
      - db
    volumes:
      - ./backend:/app
"""
    # Append right before volumes:
    docker_content = docker_content.replace("\nvolumes:\n  postgres_data:", injection + "\nvolumes:\n  postgres_data:")
    
    # Also update backend to depend on redis
    docker_content = docker_content.replace(
        "    environment:\n      - DATABASE_URL=postgresql://postgres:postgres@db:5432/healthsphere",
        "    environment:\n      - DATABASE_URL=postgresql://postgres:postgres@db:5432/healthsphere\n      - REDIS_URL=redis://redis:6379/0"
    )
    
    with open(path_docker, "w") as f:
        f.write(docker_content)

print("Celery and Redis architecture integrated.")
