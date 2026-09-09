from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.billing import Invoice
from app.schemas.enterprise import InvoiceCreate

router = APIRouter(prefix="/api/billing", tags=["Billing & Invoicing"])

@router.post("/invoices")
def create_invoice(inv: InvoiceCreate, db: Session = Depends(get_db)):
    db_inv = Invoice(**inv.dict())
    db.add(db_inv)
    db.commit()
    return {"id": db_inv.id}
