
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.oncology.schema import OncologyCreate, OncologyResponse
from app.crud.oncology import crud

router = APIRouter(prefix="/api/oncology", tags=["Oncology"])

@router.post("/", response_model=OncologyResponse)
def create_oncology_endpoint(record: OncologyCreate, db: Session = Depends(get_db)):
    return crud.create_oncology_record(db=db, record=record)

@router.get("/", response_model=List[OncologyResponse])
def read_oncology_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_oncology_records(db, skip=skip, limit=limit)
