import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# Patient Schemas
create_file('backend/app/schemas/patient.py', """
from pydantic import BaseModel, UUID4
from datetime import date, datetime
from typing import Optional
from app.models.patient import BloodGroup
from app.schemas.user import UserResponse

class PatientBase(BaseModel):
    date_of_birth: date
    gender: str
    blood_group: Optional[BloodGroup] = None
    address: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_number: Optional[str] = None

class PatientCreate(PatientBase):
    user_id: UUID4

class PatientUpdate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: UUID4
    user_id: UUID4
    created_at: datetime
    updated_at: datetime
    user: Optional[UserResponse] = None

    class Config:
        from_attributes = True
""")

# Patient API Routes
create_file('backend/app/api/patients.py', """
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.db.database import get_db
from app.api.deps import get_current_user, get_current_active_admin, get_current_doctor
from app.models.patient import Patient
from app.models.user import User, UserRole
from app.schemas.patient import PatientCreate, PatientResponse, PatientUpdate

router = APIRouter(prefix="/api/patients", tags=["Patients"])

@router.get("/", response_model=List[PatientResponse])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_doctor)):
    # Only doctors, nurses, and admins can list patients
    patients = db.query(Patient).offset(skip).limit(limit).all()
    return patients

@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
        
    # Patients can only view their own profile unless they are staff
    if current_user.role == UserRole.PATIENT and str(patient.user_id) != str(current_user.id):
        raise HTTPException(status_code=403, detail="Not authorized to view this patient")
        
    return patient

@router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(patient_in: PatientCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_admin)):
    # Ensure user exists
    user = db.query(User).filter(User.id == patient_in.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    db_patient = Patient(**patient_in.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: UUID, patient_in: PatientUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_doctor)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
        
    update_data = patient_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(patient, key, value)
        
    db.commit()
    db.refresh(patient)
    return patient
""")

# Update Main.py
create_file('update_main_patients.py', """
import os
path = 'backend/app/main.py'
with open(path, 'r') as f:
    content = f.read()

if 'from app.api import patients' not in content:
    content = content.replace('from app.api import auth', 'from app.api import auth, patients')
    content = content.replace('app.include_router(auth.router)', 'app.include_router(auth.router)\\napp.include_router(patients.router)')
    with open(path, 'w') as f:
        f.write(content)
""")

print("Patient API generated successfully.")
