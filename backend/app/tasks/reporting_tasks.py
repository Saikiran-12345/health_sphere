import time
from app.core.celery_app import celery_app

@celery_app.task(name="generate_monthly_financial_report")
def generate_monthly_financial_report():
    """
    Simulates a heavy pandas aggregation task running via Celery Beat.
    """
    print("[CELERY] Starting heavy financial aggregation...")
    time.sleep(5)  # Simulate massive DB querying and PDF writing
    print("[CELERY] Financial report generated and saved to S3.")
    return True
