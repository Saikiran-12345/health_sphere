
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.procurement.schema import ProcurementCreate, ProcurementResponse
from app.crud.procurement import crud

router = APIRouter(prefix="/api/procurement", tags=["Procurement"])

@router.post("/", response_model=ProcurementResponse)
def create_procurement_endpoint(record: ProcurementCreate, db: Session = Depends(get_db)):
    return crud.create_procurement_record(db=db, record=record)

@router.get("/", response_model=List[ProcurementResponse])
def read_procurement_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_procurement_records(db, skip=skip, limit=limit)
