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
