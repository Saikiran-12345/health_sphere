
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.surgery.schema import SurgeryCreate, SurgeryResponse
from app.crud.surgery import crud

router = APIRouter(prefix="/api/surgery", tags=["Surgery"])

@router.post("/", response_model=SurgeryResponse)
def create_surgery_endpoint(record: SurgeryCreate, db: Session = Depends(get_db)):
    return crud.create_surgery_record(db=db, record=record)

@router.get("/", response_model=List[SurgeryResponse])
def read_surgery_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_surgery_records(db, skip=skip, limit=limit)
