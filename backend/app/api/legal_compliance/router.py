
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.legal_compliance.schema import Legal_complianceCreate, Legal_complianceResponse
from app.crud.legal_compliance import crud

router = APIRouter(prefix="/api/legal_compliance", tags=["Legal_compliance"])

@router.post("/", response_model=Legal_complianceResponse)
def create_legal_compliance_endpoint(record: Legal_complianceCreate, db: Session = Depends(get_db)):
    return crud.create_legal_compliance_record(db=db, record=record)

@router.get("/", response_model=List[Legal_complianceResponse])
def read_legal_compliance_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_legal_compliance_records(db, skip=skip, limit=limit)
