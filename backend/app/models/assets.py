from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Asset(BaseModel):
    __tablename__ = "assets"
    name = Column(String(255), nullable=False)
    serial_number = Column(String(100), unique=True, nullable=False)
    category = Column(String(100), nullable=False) # IMAGING, SURGICAL, TRANSPORT, IT
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=True)
    purchase_date = Column(DateTime, nullable=False)
    last_maintenance = Column(DateTime, nullable=True)
    status = Column(String(50), default="OPERATIONAL") # OPERATIONAL, MAINTENANCE, DECOMMISSIONED

class MaintenanceLog(BaseModel):
    __tablename__ = "maintenance_logs"
    asset_id = Column(UUID(as_uuid=True), ForeignKey("assets.id"), nullable=False)
    technician = Column(String(100), nullable=False)
    issue_description = Column(String(500), nullable=False)
    resolution = Column(String(500), nullable=True)
    cost = Column(Float, default=0.0)
    date_logged = Column(DateTime, nullable=False)
