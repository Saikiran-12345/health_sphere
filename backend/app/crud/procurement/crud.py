
from sqlalchemy.orm import Session
from app.models.procurement.model import ProcurementRecord
from app.schemas.procurement.schema import ProcurementCreate

def get_procurement_record(db: Session, record_id: str):
    return db.query(ProcurementRecord).filter(ProcurementRecord.id == record_id).first()

def get_procurement_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProcurementRecord).offset(skip).limit(limit).all()

def create_procurement_record(db: Session, record: ProcurementCreate):
    db_record = ProcurementRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
