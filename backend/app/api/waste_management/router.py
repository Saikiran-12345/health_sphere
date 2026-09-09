
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.waste_management.schema import Waste_managementCreate, Waste_managementResponse
from app.crud.waste_management import crud

router = APIRouter(prefix="/api/waste_management", tags=["Waste_management"])

@router.post("/", response_model=Waste_managementResponse)
def create_waste_management_endpoint(record: Waste_managementCreate, db: Session = Depends(get_db)):
    return crud.create_waste_management_record(db=db, record=record)

@router.get("/", response_model=List[Waste_managementResponse])
def read_waste_management_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_waste_management_records(db, skip=skip, limit=limit)
