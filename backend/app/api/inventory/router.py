
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.inventory.schema import InventoryCreate, InventoryResponse
from app.crud.inventory import crud

router = APIRouter(prefix="/api/inventory", tags=["Inventory"])

@router.post("/", response_model=InventoryResponse)
def create_inventory_endpoint(record: InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory_record(db=db, record=record)

@router.get("/", response_model=List[InventoryResponse])
def read_inventory_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_inventory_records(db, skip=skip, limit=limit)
