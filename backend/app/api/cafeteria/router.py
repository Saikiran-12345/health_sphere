
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.cafeteria.schema import CafeteriaCreate, CafeteriaResponse
from app.crud.cafeteria import crud

router = APIRouter(prefix="/api/cafeteria", tags=["Cafeteria"])

@router.post("/", response_model=CafeteriaResponse)
def create_cafeteria_endpoint(record: CafeteriaCreate, db: Session = Depends(get_db)):
    return crud.create_cafeteria_record(db=db, record=record)

@router.get("/", response_model=List[CafeteriaResponse])
def read_cafeteria_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cafeteria_records(db, skip=skip, limit=limit)
