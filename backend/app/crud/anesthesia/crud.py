
from sqlalchemy.orm import Session
from app.models.anesthesia.model import AnesthesiaRecord
from app.schemas.anesthesia.schema import AnesthesiaCreate

def get_anesthesia_record(db: Session, record_id: str):
    return db.query(AnesthesiaRecord).filter(AnesthesiaRecord.id == record_id).first()

def get_anesthesia_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AnesthesiaRecord).offset(skip).limit(limit).all()

def create_anesthesia_record(db: Session, record: AnesthesiaCreate):
    db_record = AnesthesiaRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
