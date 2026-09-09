import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Models
create_file('backend/app/models/operations.py', """
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
""")

# 2. Schemas
create_file('backend/app/schemas/operations.py', """
from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class BedResponse(BaseModel):
    id: UUID4
    ward_id: UUID4
    bed_number: str
    is_occupied: bool
    status: str
    class Config: from_attributes = True

class AdmissionCreate(BaseModel):
    patient_id: UUID4
    bed_id: UUID4
    admitting_doctor_id: UUID4
    admission_date: datetime
    reason_for_admission: str
""")

# 3. API
create_file('backend/app/api/operations.py', """
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.operations import Bed, Admission, Ward, Surgery
from app.schemas.operations import BedResponse, AdmissionCreate
from typing import List

router = APIRouter(prefix="/api/ops", tags=["Hospital Operations"])

@router.get("/beds", response_model=List[BedResponse])
def get_beds(db: Session = Depends(get_db)):
    return db.query(Bed).all()

@router.post("/admit")
def admit_patient(admin_in: AdmissionCreate, db: Session = Depends(get_db)):
    bed = db.query(Bed).filter(Bed.id == admin_in.bed_id).first()
    if not bed or bed.is_occupied:
        raise HTTPException(status_code=400, detail="Bed is unavailable")
        
    bed.is_occupied = True
    bed.status = "OCCUPIED"
    
    db_admission = Admission(**admin_in.dict())
    db.add(db_admission)
    db.commit()
    return {"status": "success", "admission_id": db_admission.id}
""")

# Update main.py and __init__.py
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import operations" not in content:
    content = content.replace("from app.api import auth, patients, clinical, pharmacy, laboratory, ai", "from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations")
    content += "\napp.include_router(operations.router)\n"
    with open(path, "w") as f:
        f.write(content)

path2 = "backend/app/models/__init__.py"
with open(path2, "a") as f:
    f.write("\nfrom app.models.operations import Ward, Bed, Admission, Surgery\n")

print("Hospital Ops Generated.")
