from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Ward(BaseModel):
    __tablename__ = "wards"
    name = Column(String(100), unique=True, nullable=False)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=False)
    capacity = Column(Integer, default=0)
    ward_type = Column(String(50), nullable=False) # ICU, GENERAL, MATERNITY

class Bed(BaseModel):
    __tablename__ = "beds"
    ward_id = Column(UUID(as_uuid=True), ForeignKey("wards.id"), nullable=False)
    bed_number = Column(String(20), unique=True, nullable=False)
    is_occupied = Column(Boolean, default=False)
    status = Column(String(50), default="AVAILABLE") # AVAILABLE, OCCUPIED, MAINTENANCE

class Admission(BaseModel):
    __tablename__ = "admissions"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    bed_id = Column(UUID(as_uuid=True), ForeignKey("beds.id"), nullable=False)
    admitting_doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    
    admission_date = Column(DateTime, nullable=False)
    discharge_date = Column(DateTime, nullable=True)
    status = Column(String(50), default="ADMITTED") # ADMITTED, DISCHARGED, TRANSFERRED
    reason_for_admission = Column(Text, nullable=False)

class Surgery(BaseModel):
    __tablename__ = "surgeries"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    lead_surgeon_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    
    surgery_name = Column(String(255), nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    theatre_number = Column(String(50), nullable=False)
    status = Column(String(50), default="SCHEDULED") # SCHEDULED, IN_PROGRESS, COMPLETED
    pre_op_notes = Column(Text, nullable=True)
    post_op_notes = Column(Text, nullable=True)
