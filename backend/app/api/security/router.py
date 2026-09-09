
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.security.schema import SecurityCreate, SecurityResponse
from app.crud.security import crud

router = APIRouter(prefix="/api/security", tags=["Security"])

@router.post("/", response_model=SecurityResponse)
def create_security_endpoint(record: SecurityCreate, db: Session = Depends(get_db)):
    return crud.create_security_record(db=db, record=record)

@router.get("/", response_model=List[SecurityResponse])
def read_security_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_security_records(db, skip=skip, limit=limit)
