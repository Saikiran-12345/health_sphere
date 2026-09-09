
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.mortuary.schema import MortuaryCreate, MortuaryResponse
from app.crud.mortuary import crud

router = APIRouter(prefix="/api/mortuary", tags=["Mortuary"])

@router.post("/", response_model=MortuaryResponse)
def create_mortuary_endpoint(record: MortuaryCreate, db: Session = Depends(get_db)):
    return crud.create_mortuary_record(db=db, record=record)

@router.get("/", response_model=List[MortuaryResponse])
def read_mortuary_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_mortuary_records(db, skip=skip, limit=limit)
