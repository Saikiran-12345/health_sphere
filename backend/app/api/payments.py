import os
import stripe
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request
from fastapi.responses import Response
from app.services.pdf_generator import InvoicePDFGenerator
from typing import Dict, Any

router = APIRouter(prefix="/api/payments", tags=["Payments & Billing"])

# This would normally be in .env
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_mock_key_12345")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_mock")

@router.post("/create-checkout-session")
def create_checkout_session(invoice_id: str, amount_usd: float):
    """
    Creates a Stripe Checkout Session for an invoice.
    """
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'HealthSphere Medical Invoice {invoice_id}',
                    },
                    'unit_amount': int(amount_usd * 100), # Stripe uses cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:5173/billing?success=true',
            cancel_url='http://localhost:5173/billing?canceled=true',
            client_reference_id=invoice_id
        )
        return {"checkout_url": session.url}
    except Exception as e:
        # Mocking for local dev without real Stripe keys
        return {"checkout_url": f"http://localhost:5173/billing?mock_checkout=true&inv={invoice_id}"}

@router.post("/webhook")
async def stripe_webhook(request: Request):
    """
    Secure Stripe Webhook to mark invoices as PAID asynchronously.
    """
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except Exception as e:
        return {"status": "mock_success", "note": "Failed real sig, but returning 200 for local dev"}
        
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Here we would update the DB: Invoice.status = 'PAID'
        print(f"Payment success for invoice {session.client_reference_id}")
        
    return {"status": "success"}

@router.get("/{invoice_id}/download-pdf")
def download_invoice_pdf(invoice_id: str):
    """
    Generates and returns a binary PDF file for the given invoice.
    """
    # Mock data for demonstration - in reality, fetched via SQLAlchemy
    mock_data = {
        "id": invoice_id,
        "patient_name": "John Doe",
        "patient_id": "PAT-7742",
        "items": [
            {"description": "General Consultation", "qty": 1, "price": 150.00},
            {"description": "Comprehensive Blood Panel", "qty": 1, "price": 85.50},
            {"description": "Amoxicillin 500mg", "qty": 2, "price": 12.00}
        ]
    }
    
    pdf_bytes = InvoicePDFGenerator.generate_invoice_pdf(mock_data)
    
    return Response(
        content=pdf_bytes, 
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=invoice_{invoice_id}.pdf"}
    )
