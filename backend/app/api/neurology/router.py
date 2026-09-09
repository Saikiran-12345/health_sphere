
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.neurology.schema import NeurologyCreate, NeurologyResponse
from app.crud.neurology import crud

router = APIRouter(prefix="/api/neurology", tags=["Neurology"])

@router.post("/", response_model=NeurologyResponse)
def create_neurology_endpoint(record: NeurologyCreate, db: Session = Depends(get_db)):
    return crud.create_neurology_record(db=db, record=record)

@router.get("/", response_model=List[NeurologyResponse])
def read_neurology_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_neurology_records(db, skip=skip, limit=limit)
