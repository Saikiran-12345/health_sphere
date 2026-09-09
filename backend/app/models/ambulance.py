from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Ambulance(BaseModel):
    __tablename__ = "ambulances"
    vehicle_number = Column(String(50), unique=True, nullable=False)
    vehicle_type = Column(String(50), nullable=False) # BASIC, ALS, ICU
    status = Column(String(50), default="AVAILABLE") # AVAILABLE, DISPATCHED, MAINTENANCE

class DispatchRecord(BaseModel):
    __tablename__ = "dispatch_records"
    ambulance_id = Column(UUID(as_uuid=True), ForeignKey("ambulances.id"), nullable=False)
    driver_name = Column(String(100), nullable=False)
    pickup_location = Column(String(255), nullable=False)
    emergency_type = Column(String(100), nullable=False)
    dispatch_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=True)
    status = Column(String(50), default="EN_ROUTE")
