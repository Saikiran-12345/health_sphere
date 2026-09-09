from sqlalchemy import Column, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import enum
from app.models.base import BaseModel

class RecordType(str, enum.Enum):
    CLINICAL_NOTE = "CLINICAL_NOTE"
    DIAGNOSIS = "DIAGNOSIS"
    PRESCRIPTION = "PRESCRIPTION"
    LAB_RESULT = "LAB_RESULT"
    RADIOLOGY = "RADIOLOGY"
    SURGERY_NOTE = "SURGERY_NOTE"

class MedicalRecord(BaseModel):
    __tablename__ = "medical_records"

    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    appointment_id = Column(UUID(as_uuid=True), ForeignKey("appointments.id"), nullable=True)
    
    record_type = Column(Enum(RecordType), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    attachments = Column(Text, nullable=True) # JSON array of URLs
    
    # Relationships
    patient = relationship("Patient")
    doctor = relationship("Doctor")
