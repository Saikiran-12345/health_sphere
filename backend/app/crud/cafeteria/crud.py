
from sqlalchemy.orm import Session
from app.models.cafeteria.model import CafeteriaRecord
from app.schemas.cafeteria.schema import CafeteriaCreate

def get_cafeteria_record(db: Session, record_id: str):
    return db.query(CafeteriaRecord).filter(CafeteriaRecord.id == record_id).first()

def get_cafeteria_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CafeteriaRecord).offset(skip).limit(limit).all()

def create_cafeteria_record(db: Session, record: CafeteriaCreate):
    db_record = CafeteriaRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
