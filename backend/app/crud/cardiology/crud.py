
from sqlalchemy.orm import Session
from app.models.cardiology.model import CardiologyRecord
from app.schemas.cardiology.schema import CardiologyCreate

def get_cardiology_record(db: Session, record_id: str):
    return db.query(CardiologyRecord).filter(CardiologyRecord.id == record_id).first()

def get_cardiology_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CardiologyRecord).offset(skip).limit(limit).all()

def create_cardiology_record(db: Session, record: CardiologyCreate):
    db_record = CardiologyRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
