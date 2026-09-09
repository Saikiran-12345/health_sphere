
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.sterilization.schema import SterilizationCreate, SterilizationResponse
from app.crud.sterilization import crud

router = APIRouter(prefix="/api/sterilization", tags=["Sterilization"])

@router.post("/", response_model=SterilizationResponse)
def create_sterilization_endpoint(record: SterilizationCreate, db: Session = Depends(get_db)):
    return crud.create_sterilization_record(db=db, record=record)

@router.get("/", response_model=List[SterilizationResponse])
def read_sterilization_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_sterilization_records(db, skip=skip, limit=limit)
