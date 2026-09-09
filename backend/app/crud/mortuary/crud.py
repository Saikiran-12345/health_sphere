
from sqlalchemy.orm import Session
from app.models.mortuary.model import MortuaryRecord
from app.schemas.mortuary.schema import MortuaryCreate

def get_mortuary_record(db: Session, record_id: str):
    return db.query(MortuaryRecord).filter(MortuaryRecord.id == record_id).first()

def get_mortuary_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MortuaryRecord).offset(skip).limit(limit).all()

def create_mortuary_record(db: Session, record: MortuaryCreate):
    db_record = MortuaryRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
