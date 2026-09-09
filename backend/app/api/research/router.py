
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.research.schema import ResearchCreate, ResearchResponse
from app.crud.research import crud

router = APIRouter(prefix="/api/research", tags=["Research"])

@router.post("/", response_model=ResearchResponse)
def create_research_endpoint(record: ResearchCreate, db: Session = Depends(get_db)):
    return crud.create_research_record(db=db, record=record)

@router.get("/", response_model=List[ResearchResponse])
def read_research_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_research_records(db, skip=skip, limit=limit)
