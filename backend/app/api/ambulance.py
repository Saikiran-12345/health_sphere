from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.ambulance import Ambulance, DispatchRecord
from app.schemas.enterprise import AmbulanceCreate, DispatchCreate

router = APIRouter(prefix="/api/ambulance", tags=["Ambulance Dispatch"])

@router.post("/")
def create_ambulance(amb: AmbulanceCreate, db: Session = Depends(get_db)):
    db_amb = Ambulance(**amb.dict())
    db.add(db_amb)
    db.commit()
    return db_amb
