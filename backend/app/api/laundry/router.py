
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.laundry.schema import LaundryCreate, LaundryResponse
from app.crud.laundry import crud

router = APIRouter(prefix="/api/laundry", tags=["Laundry"])

@router.post("/", response_model=LaundryResponse)
def create_laundry_endpoint(record: LaundryCreate, db: Session = Depends(get_db)):
    return crud.create_laundry_record(db=db, record=record)

@router.get("/", response_model=List[LaundryResponse])
def read_laundry_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_laundry_records(db, skip=skip, limit=limit)
