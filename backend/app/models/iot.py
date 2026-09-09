from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class VitalSignStream(BaseModel):
    __tablename__ = "iot_vital_streams"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    device_id = Column(String(100), nullable=False)
    heart_rate = Column(Float, nullable=True)
    sp02 = Column(Float, nullable=True)
    blood_pressure_sys = Column(Float, nullable=True)
    blood_pressure_dia = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)
