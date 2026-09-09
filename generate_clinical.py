import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Appointment Model
create_file('backend/app/models/appointment.py', """
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import enum
from app.models.base import BaseModel

class AppointmentStatus(str, enum.Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    CHECKED_IN = "CHECKED_IN"
    IN_CONSULTATION = "IN_CONSULTATION"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    NO_SHOW = "NO_SHOW"

class Appointment(BaseModel):
    __tablename__ = "appointments"

    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=False)
    
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(Enum(AppointmentStatus), default=AppointmentStatus.SCHEDULED, nullable=False)
    reason_for_visit = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    
    # Relationships
    patient = relationship("Patient")
    doctor = relationship("Doctor")
    department = relationship("Department")
""")

# 2. Medical Record Model
create_file('backend/app/models/medical_record.py', """
from sqlalchemy import Column, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import enum
from app.models.base import BaseModel

class RecordType(str, enum.Enum):
    CLINICAL_NOTE = "CLINICAL_NOTE"
    DIAGNOSIS = "DIAGNOSIS"
    PRESCRIPTION = "PRESCRIPTION"
    LAB_RESULT = "LAB_RESULT"
    RADIOLOGY = "RADIOLOGY"
    SURGERY_NOTE = "SURGERY_NOTE"

class MedicalRecord(BaseModel):
    __tablename__ = "medical_records"

    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"), nullable=False)
    appointment_id = Column(UUID(as_uuid=True), ForeignKey("appointments.id"), nullable=True)
    
    record_type = Column(Enum(RecordType), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    attachments = Column(Text, nullable=True) # JSON array of URLs
    
    # Relationships
    patient = relationship("Patient")
    doctor = relationship("Doctor")
""")

# 3. Schemas
create_file('backend/app/schemas/clinical.py', """
from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional
from app.models.appointment import AppointmentStatus
from app.models.medical_record import RecordType

class AppointmentBase(BaseModel):
    patient_id: UUID4
    doctor_id: UUID4
    department_id: UUID4
    scheduled_time: datetime
    reason_for_visit: Optional[str] = None
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    status: Optional[AppointmentStatus] = None
    scheduled_time: Optional[datetime] = None
    notes: Optional[str] = None

class AppointmentResponse(AppointmentBase):
    id: UUID4
    status: AppointmentStatus
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class MedicalRecordBase(BaseModel):
    patient_id: UUID4
    doctor_id: UUID4
    appointment_id: Optional[UUID4] = None
    record_type: RecordType
    title: str
    content: str
    attachments: Optional[str] = None

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecordResponse(MedicalRecordBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
""")

# 4. API Endpoints
create_file('backend/app/api/clinical.py', """
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.db.database import get_db
from app.api.deps import get_current_user, get_current_doctor
from app.models.appointment import Appointment
from app.models.medical_record import MedicalRecord
from app.models.user import User, UserRole
from app.schemas.clinical import AppointmentCreate, AppointmentUpdate, AppointmentResponse, MedicalRecordCreate, MedicalRecordResponse

router = APIRouter(prefix="/api/clinical", tags=["Clinical Core"])

@router.post("/appointments", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(appt_in: AppointmentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_appt = Appointment(**appt_in.dict())
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt

@router.get("/appointments", response_model=List[AppointmentResponse])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role == UserRole.PATIENT:
        return db.query(Appointment).filter(Appointment.patient_id == current_user.id).all()
    return db.query(Appointment).offset(skip).limit(limit).all()

@router.post("/records", response_model=MedicalRecordResponse, status_code=status.HTTP_201_CREATED)
def create_medical_record(record_in: MedicalRecordCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_doctor)):
    db_record = MedicalRecord(**record_in.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/records/{patient_id}", response_model=List[MedicalRecordResponse])
def get_patient_records(patient_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role == UserRole.PATIENT and str(current_user.id) != str(patient_id):
        raise HTTPException(status_code=403, detail="Not authorized")
    return db.query(MedicalRecord).filter(MedicalRecord.patient_id == patient_id).order_by(MedicalRecord.created_at.desc()).all()
""")

# 5. Update main.py and __init__.py
create_file('update_clinical.py', """
import os

# Update main.py
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import clinical" not in content:
    content = content.replace("from app.api import auth, patients", "from app.api import auth, patients, clinical")
    content = content.replace("app.include_router(patients.router)", "app.include_router(patients.router)\\napp.include_router(clinical.router)")
    with open(path, "w") as f:
        f.write(content)

# Update models/__init__.py
path = "backend/app/models/__init__.py"
with open(path, "r") as f:
    content = f.read()

if "from app.models.appointment import Appointment" not in content:
    content += "\\nfrom app.models.appointment import Appointment, AppointmentStatus"
    content += "\\nfrom app.models.medical_record import MedicalRecord, RecordType\\n"
    with open(path, "w") as f:
        f.write(content)
""")

print("Clinical domain generated successfully.")
