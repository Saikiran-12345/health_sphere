import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# ================= PHARMACY DOMAIN =================
create_file('backend/app/models/pharmacy.py', """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Medicine(BaseModel):
    __tablename__ = "medicines"
    name = Column(String(255), index=True, nullable=False)
    generic_name = Column(String(255), nullable=True)
    category = Column(String(100), nullable=False)
    manufacturer = Column(String(255), nullable=True)
    unit_price = Column(Float, default=0.0)
    stock_quantity = Column(Integer, default=0)
    reorder_level = Column(Integer, default=10)

class Prescription(BaseModel):
    __tablename__ = "prescriptions"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    appointment_id = Column(UUID(as_uuid=True), ForeignKey("appointments.id"), nullable=True)
    status = Column(String(50), default="PENDING") # PENDING, DISPENSED, CANCELLED
    notes = Column(Text, nullable=True)

class PrescriptionItem(BaseModel):
    __tablename__ = "prescription_items"
    prescription_id = Column(UUID(as_uuid=True), ForeignKey("prescriptions.id"), nullable=False)
    medicine_id = Column(UUID(as_uuid=True), ForeignKey("medicines.id"), nullable=False)
    dosage = Column(String(100), nullable=False)
    frequency = Column(String(100), nullable=False)
    duration_days = Column(Integer, nullable=False)
    quantity_dispensed = Column(Integer, default=0)
""")

create_file('backend/app/schemas/pharmacy.py', """
from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional, List

class MedicineBase(BaseModel):
    name: str
    generic_name: Optional[str] = None
    category: str
    manufacturer: Optional[str] = None
    unit_price: float
    stock_quantity: int
    reorder_level: int

class MedicineCreate(MedicineBase): pass

class MedicineResponse(MedicineBase):
    id: UUID4
    class Config: from_attributes = True

class PrescriptionItemBase(BaseModel):
    medicine_id: UUID4
    dosage: str
    frequency: str
    duration_days: int

class PrescriptionCreate(BaseModel):
    patient_id: UUID4
    appointment_id: Optional[UUID4] = None
    notes: Optional[str] = None
    items: List[PrescriptionItemBase]
""")

create_file('backend/app/api/pharmacy.py', """
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.db.database import get_db
from app.api.deps import get_current_user, get_current_doctor
from app.models.pharmacy import Medicine, Prescription, PrescriptionItem
from app.schemas.pharmacy import MedicineCreate, MedicineResponse, PrescriptionCreate

router = APIRouter(prefix="/api/pharmacy", tags=["Pharmacy"])

@router.get("/medicines", response_model=List[MedicineResponse])
def get_medicines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Medicine).offset(skip).limit(limit).all()

@router.post("/medicines", response_model=MedicineResponse)
def create_medicine(med_in: MedicineCreate, db: Session = Depends(get_db)):
    db_med = Medicine(**med_in.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

@router.post("/prescriptions")
def create_prescription(pres_in: PrescriptionCreate, db: Session = Depends(get_db), current_user=Depends(get_current_doctor)):
    doctor = db.query(current_user.__class__).filter(current_user.__class__.id == current_user.id).first()
    db_pres = Prescription(patient_id=pres_in.patient_id, doctor_id=current_user.id, appointment_id=pres_in.appointment_id, notes=pres_in.notes)
    db.add(db_pres)
    db.commit()
    db.refresh(db_pres)
    
    for item in pres_in.items:
        db_item = PrescriptionItem(prescription_id=db_pres.id, **item.dict())
        db.add(db_item)
    db.commit()
    return {"status": "success", "prescription_id": db_pres.id}
""")

# ================= LABORATORY DOMAIN =================
create_file('backend/app/models/laboratory.py', """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class LabTest(BaseModel):
    __tablename__ = "lab_tests"
    name = Column(String(255), index=True, nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, default=0.0)

class LabOrder(BaseModel):
    __tablename__ = "lab_orders"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    test_id = Column(UUID(as_uuid=True), ForeignKey("lab_tests.id"), nullable=False)
    status = Column(String(50), default="ORDERED") # ORDERED, COLLECTED, PROCESSING, COMPLETED
    result_value = Column(Text, nullable=True)
    remarks = Column(Text, nullable=True)
""")

create_file('backend/app/api/laboratory.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.laboratory import LabTest, LabOrder

router = APIRouter(prefix="/api/laboratory", tags=["Laboratory"])

@router.get("/tests")
def get_tests(db: Session = Depends(get_db)):
    return db.query(LabTest).all()
""")

# Update main.py and __init__.py
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import pharmacy" not in content:
    content = content.replace("from app.api import auth, patients, clinical", "from app.api import auth, patients, clinical, pharmacy, laboratory")
    content += "\napp.include_router(pharmacy.router)\napp.include_router(laboratory.router)\n"
    with open(path, "w") as f:
        f.write(content)

path2 = "backend/app/models/__init__.py"
with open(path2, "a") as f:
    f.write("\nfrom app.models.pharmacy import Medicine, Prescription, PrescriptionItem")
    f.write("\nfrom app.models.laboratory import LabTest, LabOrder\n")

print("Massive Medical Domains generated successfully.")
