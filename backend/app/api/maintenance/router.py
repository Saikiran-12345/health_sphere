
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.maintenance.schema import MaintenanceCreate, MaintenanceResponse
from app.crud.maintenance import crud

router = APIRouter(prefix="/api/maintenance", tags=["Maintenance"])

@router.post("/", response_model=MaintenanceResponse)
def create_maintenance_endpoint(record: MaintenanceCreate, db: Session = Depends(get_db)):
    return crud.create_maintenance_record(db=db, record=record)

@router.get("/", response_model=List[MaintenanceResponse])
def read_maintenance_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_maintenance_records(db, skip=skip, limit=limit)
