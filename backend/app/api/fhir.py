from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.database import get_db
from app.models.patient import Patient
from app.services.fhir import FHIRMapper

router = APIRouter(prefix="/fhir/r4", tags=["FHIR Interoperability"])

@router.get("/Patient/{patient_id}")
def get_fhir_patient(patient_id: UUID, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return FHIRMapper.patient_to_fhir(patient)
