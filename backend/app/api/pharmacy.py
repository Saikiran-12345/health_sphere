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
