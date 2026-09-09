
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.transport.schema import TransportCreate, TransportResponse
from app.crud.transport import crud

router = APIRouter(prefix="/api/transport", tags=["Transport"])

@router.post("/", response_model=TransportResponse)
def create_transport_endpoint(record: TransportCreate, db: Session = Depends(get_db)):
    return crud.create_transport_record(db=db, record=record)

@router.get("/", response_model=List[TransportResponse])
def read_transport_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transport_records(db, skip=skip, limit=limit)
