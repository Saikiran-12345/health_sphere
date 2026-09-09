
from sqlalchemy.orm import Session
from app.models.inventory.model import InventoryRecord
from app.schemas.inventory.schema import InventoryCreate

def get_inventory_record(db: Session, record_id: str):
    return db.query(InventoryRecord).filter(InventoryRecord.id == record_id).first()

def get_inventory_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InventoryRecord).offset(skip).limit(limit).all()

def create_inventory_record(db: Session, record: InventoryCreate):
    db_record = InventoryRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
