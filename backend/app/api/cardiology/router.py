
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.cardiology.schema import CardiologyCreate, CardiologyResponse
from app.crud.cardiology import crud

router = APIRouter(prefix="/api/cardiology", tags=["Cardiology"])

@router.post("/", response_model=CardiologyResponse)
def create_cardiology_endpoint(record: CardiologyCreate, db: Session = Depends(get_db)):
    return crud.create_cardiology_record(db=db, record=record)

@router.get("/", response_model=List[CardiologyResponse])
def read_cardiology_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cardiology_records(db, skip=skip, limit=limit)
