from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class LabTest(BaseModel):
    __tablename__ = "lab_tests"
    name = Column(String(255), index=True, nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, default=0.0)

class LabOrder(BaseModel):
    __tablename__ = "lab_orders"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    test_id = Column(UUID(as_uuid=True), ForeignKey("lab_tests.id"), nullable=False)
    status = Column(String(50), default="ORDERED") # ORDERED, COLLECTED, PROCESSING, COMPLETED
    result_value = Column(Text, nullable=True)
    remarks = Column(Text, nullable=True)
