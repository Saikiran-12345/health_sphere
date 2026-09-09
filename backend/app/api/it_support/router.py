
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.it_support.schema import It_supportCreate, It_supportResponse
from app.crud.it_support import crud

router = APIRouter(prefix="/api/it_support", tags=["It_support"])

@router.post("/", response_model=It_supportResponse)
def create_it_support_endpoint(record: It_supportCreate, db: Session = Depends(get_db)):
    return crud.create_it_support_record(db=db, record=record)

@router.get("/", response_model=List[It_supportResponse])
def read_it_support_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_it_support_records(db, skip=skip, limit=limit)
