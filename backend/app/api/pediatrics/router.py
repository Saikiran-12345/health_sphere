
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.pediatrics.schema import PediatricsCreate, PediatricsResponse
from app.crud.pediatrics import crud

router = APIRouter(prefix="/api/pediatrics", tags=["Pediatrics"])

@router.post("/", response_model=PediatricsResponse)
def create_pediatrics_endpoint(record: PediatricsCreate, db: Session = Depends(get_db)):
    return crud.create_pediatrics_record(db=db, record=record)

@router.get("/", response_model=List[PediatricsResponse])
def read_pediatrics_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_pediatrics_records(db, skip=skip, limit=limit)
