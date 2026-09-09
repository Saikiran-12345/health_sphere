from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Doctor(BaseModel):
    __tablename__ = "doctors"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=False)
    
    specialization = Column(String(100), nullable=False)
    license_number = Column(String(100), unique=True, nullable=False)
    consultation_fee = Column(Integer, default=0)
    bio = Column(Text, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="doctor_profile")
    department = relationship("Department", back_populates="doctors")
