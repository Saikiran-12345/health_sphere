from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Medicine(BaseModel):
    __tablename__ = "medicines"
    name = Column(String(255), index=True, nullable=False)
    generic_name = Column(String(255), nullable=True)
    category = Column(String(100), nullable=False)
    manufacturer = Column(String(255), nullable=True)
    unit_price = Column(Float, default=0.0)
    stock_quantity = Column(Integer, default=0)
    reorder_level = Column(Integer, default=10)

class Prescription(BaseModel):
    __tablename__ = "prescriptions"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    appointment_id = Column(UUID(as_uuid=True), ForeignKey("appointments.id"), nullable=True)
    status = Column(String(50), default="PENDING") # PENDING, DISPENSED, CANCELLED
    notes = Column(Text, nullable=True)

class PrescriptionItem(BaseModel):
    __tablename__ = "prescription_items"
    prescription_id = Column(UUID(as_uuid=True), ForeignKey("prescriptions.id"), nullable=False)
    medicine_id = Column(UUID(as_uuid=True), ForeignKey("medicines.id"), nullable=False)
    dosage = Column(String(100), nullable=False)
    frequency = Column(String(100), nullable=False)
    duration_days = Column(Integer, nullable=False)
    quantity_dispensed = Column(Integer, default=0)
