
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.maternity.schema import MaternityCreate, MaternityResponse
from app.crud.maternity import crud

router = APIRouter(prefix="/api/maternity", tags=["Maternity"])

@router.post("/", response_model=MaternityResponse)
def create_maternity_endpoint(record: MaternityCreate, db: Session = Depends(get_db)):
    return crud.create_maternity_record(db=db, record=record)

@router.get("/", response_model=List[MaternityResponse])
def read_maternity_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_maternity_records(db, skip=skip, limit=limit)
