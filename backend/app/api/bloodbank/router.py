
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.bloodbank.schema import BloodbankCreate, BloodbankResponse
from app.crud.bloodbank import crud

router = APIRouter(prefix="/api/bloodbank", tags=["Bloodbank"])

@router.post("/", response_model=BloodbankResponse)
def create_bloodbank_endpoint(record: BloodbankCreate, db: Session = Depends(get_db)):
    return crud.create_bloodbank_record(db=db, record=record)

@router.get("/", response_model=List[BloodbankResponse])
def read_bloodbank_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_bloodbank_records(db, skip=skip, limit=limit)
