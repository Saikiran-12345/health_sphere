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
