
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.radiology.schema import RadiologyCreate, RadiologyResponse
from app.crud.radiology import crud

router = APIRouter(prefix="/api/radiology", tags=["Radiology"])

@router.post("/", response_model=RadiologyResponse)
def create_radiology_endpoint(record: RadiologyCreate, db: Session = Depends(get_db)):
    return crud.create_radiology_record(db=db, record=record)

@router.get("/", response_model=List[RadiologyResponse])
def read_radiology_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_radiology_records(db, skip=skip, limit=limit)
