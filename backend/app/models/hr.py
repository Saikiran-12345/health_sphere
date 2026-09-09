from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class EmployeeContract(BaseModel):
    __tablename__ = "employee_contracts"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    base_salary = Column(Float, nullable=False)
    contract_start = Column(DateTime, nullable=False)
    contract_end = Column(DateTime, nullable=True)
    status = Column(String(50), default="ACTIVE")

class Payroll(BaseModel):
    __tablename__ = "payrolls"
    contract_id = Column(UUID(as_uuid=True), ForeignKey("employee_contracts.id"), nullable=False)
    month_year = Column(String(20), nullable=False) # e.g. "09-2026"
    gross_pay = Column(Float, nullable=False)
    deductions = Column(Float, default=0.0)
    net_pay = Column(Float, nullable=False)
    status = Column(String(50), default="PENDING") # PENDING, PROCESSED, PAID
