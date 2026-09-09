
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.pathology.schema import PathologyCreate, PathologyResponse
from app.crud.pathology import crud

router = APIRouter(prefix="/api/pathology", tags=["Pathology"])

@router.post("/", response_model=PathologyResponse)
def create_pathology_endpoint(record: PathologyCreate, db: Session = Depends(get_db)):
    return crud.create_pathology_record(db=db, record=record)

@router.get("/", response_model=List[PathologyResponse])
def read_pathology_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_pathology_records(db, skip=skip, limit=limit)
