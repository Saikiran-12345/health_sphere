
from sqlalchemy.orm import Session
from app.models.transport.model import TransportRecord
from app.schemas.transport.schema import TransportCreate

def get_transport_record(db: Session, record_id: str):
    return db.query(TransportRecord).filter(TransportRecord.id == record_id).first()

def get_transport_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TransportRecord).offset(skip).limit(limit).all()

def create_transport_record(db: Session, record: TransportCreate):
    db_record = TransportRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
