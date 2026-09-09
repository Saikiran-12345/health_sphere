
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.anesthesia.schema import AnesthesiaCreate, AnesthesiaResponse
from app.crud.anesthesia import crud

router = APIRouter(prefix="/api/anesthesia", tags=["Anesthesia"])

@router.post("/", response_model=AnesthesiaResponse)
def create_anesthesia_endpoint(record: AnesthesiaCreate, db: Session = Depends(get_db)):
    return crud.create_anesthesia_record(db=db, record=record)

@router.get("/", response_model=List[AnesthesiaResponse])
def read_anesthesia_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_anesthesia_records(db, skip=skip, limit=limit)
