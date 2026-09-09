from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Staff(BaseModel):
    __tablename__ = "staff"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    employee_id = Column(String(50), unique=True, nullable=False)
    designation = Column(String(100), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="staff_profile")
