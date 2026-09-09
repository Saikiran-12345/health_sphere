
from sqlalchemy.orm import Session
from app.models.research.model import ResearchRecord
from app.schemas.research.schema import ResearchCreate

def get_research_record(db: Session, record_id: str):
    return db.query(ResearchRecord).filter(ResearchRecord.id == record_id).first()

def get_research_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ResearchRecord).offset(skip).limit(limit).all()

def create_research_record(db: Session, record: ResearchCreate):
    db_record = ResearchRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
