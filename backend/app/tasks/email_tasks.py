import time
from app.core.celery_app import celery_app

@celery_app.task(name="send_invoice_email")
def send_invoice_email(invoice_id: str, patient_email: str):
    """
    Simulates sending an invoice PDF via email synchronously in the background.
    """
    # In a real app, this would use smtplib or SendGrid API
    print(f"[CELERY] Preparing to send invoice {invoice_id} to {patient_email}...")
    time.sleep(2)  # Simulate network latency
    print(f"[CELERY] Successfully dispatched invoice email to {patient_email}.")
    return {"status": "success", "invoice_id": invoice_id}
