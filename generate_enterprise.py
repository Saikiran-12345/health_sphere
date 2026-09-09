import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Billing Models
create_file('backend/app/models/billing.py', """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Invoice(BaseModel):
    __tablename__ = "invoices"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    total_amount = Column(Float, default=0.0)
    paid_amount = Column(Float, default=0.0)
    status = Column(String(50), default="PENDING") # PENDING, PARTIAL, PAID, VOID
    issued_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)

class InvoiceItem(BaseModel):
    __tablename__ = "invoice_items"
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"), nullable=False)
    description = Column(String(255), nullable=False)
    quantity = Column(Integer, default=1)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

class InsuranceClaim(BaseModel):
    __tablename__ = "insurance_claims"
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"), nullable=False)
    provider_name = Column(String(255), nullable=False)
    policy_number = Column(String(255), nullable=False)
    claim_amount = Column(Float, nullable=False)
    status = Column(String(50), default="SUBMITTED") # SUBMITTED, APPROVED, DENIED
""")

# 2. HR & Payroll Models
create_file('backend/app/models/hr.py', """
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
""")

# 3. Ambulance Dispatch Models
create_file('backend/app/models/ambulance.py', """
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
""")

# 4. Schemas
create_file('backend/app/schemas/enterprise.py', """
from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional

class InvoiceCreate(BaseModel):
    patient_id: UUID4
    issued_date: datetime
    due_date: datetime
    
class AmbulanceCreate(BaseModel):
    vehicle_number: str
    vehicle_type: str

class DispatchCreate(BaseModel):
    ambulance_id: UUID4
    driver_name: str
    pickup_location: str
    emergency_type: str
    dispatch_time: datetime
""")

# 5. APIs
create_file('backend/app/api/billing.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.billing import Invoice
from app.schemas.enterprise import InvoiceCreate

router = APIRouter(prefix="/api/billing", tags=["Billing & Invoicing"])

@router.post("/invoices")
def create_invoice(inv: InvoiceCreate, db: Session = Depends(get_db)):
    db_inv = Invoice(**inv.dict())
    db.add(db_inv)
    db.commit()
    return {"id": db_inv.id}
""")

create_file('backend/app/api/hr.py', """
from fastapi import APIRouter
router = APIRouter(prefix="/api/hr", tags=["HR & Payroll"])

@router.get("/payroll")
def get_payroll():
    return []
""")

create_file('backend/app/api/ambulance.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.ambulance import Ambulance, DispatchRecord
from app.schemas.enterprise import AmbulanceCreate, DispatchCreate

router = APIRouter(prefix="/api/ambulance", tags=["Ambulance Dispatch"])

@router.post("/")
def create_ambulance(amb: AmbulanceCreate, db: Session = Depends(get_db)):
    db_amb = Ambulance(**amb.dict())
    db.add(db_amb)
    db.commit()
    return db_amb
""")

# 6. Update Main and Models
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import billing" not in content:
    content = content.replace("from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations", 
                              "from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance")
    content += "\napp.include_router(billing.router)\napp.include_router(hr.router)\napp.include_router(ambulance.router)\n"
    with open(path, "w") as f:
        f.write(content)

path2 = "backend/app/models/__init__.py"
with open(path2, "a") as f:
    f.write("\nfrom app.models.billing import Invoice, InvoiceItem, InsuranceClaim\n")
    f.write("from app.models.hr import EmployeeContract, Payroll\n")
    f.write("from app.models.ambulance import Ambulance, DispatchRecord\n")

print("Enterprise domains added successfully.")
