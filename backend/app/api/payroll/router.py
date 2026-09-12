
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.payroll.schema import PayrollCreate, PayrollResponse
from app.crud.payroll import crud

router = APIRouter(prefix="/api/payroll", tags=["Payroll"])

@router.post("/", response_model=PayrollResponse)
def create_payroll_endpoint(record: PayrollCreate, db: Session = Depends(get_db)):
    return crud.create_payroll_record(db=db, record=record)

@router.get("/", response_model=List[PayrollResponse])
def read_payroll_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_payroll_records(db, skip=skip, limit=limit)
