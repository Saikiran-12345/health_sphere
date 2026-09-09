
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.grants.schema import GrantsCreate, GrantsResponse
from app.crud.grants import crud

router = APIRouter(prefix="/api/grants", tags=["Grants"])

@router.post("/", response_model=GrantsResponse)
def create_grants_endpoint(record: GrantsCreate, db: Session = Depends(get_db)):
    return crud.create_grants_record(db=db, record=record)

@router.get("/", response_model=List[GrantsResponse])
def read_grants_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_grants_records(db, skip=skip, limit=limit)
