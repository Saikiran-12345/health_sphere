from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Invoice(BaseModel):
    __tablename__ = "invoices"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    total_amount = Column(Float, default=0.0)
    paid_amount = Column(Float, default=0.0)
    status = Column(String(50), default="PENDING") # PENDING, PARTIAL, PAID, VOID
    issued_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)

class InvoiceItem(BaseModel):
    __tablename__ = "invoice_items"
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"), nullable=False)
    description = Column(String(255), nullable=False)
    quantity = Column(Integer, default=1)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

class InsuranceClaim(BaseModel):
    __tablename__ = "insurance_claims"
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"), nullable=False)
    provider_name = Column(String(255), nullable=False)
    policy_number = Column(String(255), nullable=False)
    claim_amount = Column(Float, nullable=False)
    status = Column(String(50), default="SUBMITTED") # SUBMITTED, APPROVED, DENIED
