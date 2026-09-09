from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Department(BaseModel):
    __tablename__ = "departments"

    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    contact_number = Column(String(20), nullable=True)
    location = Column(String(100), nullable=True)
    
    # Relationships
    doctors = relationship("Doctor", back_populates="department")
