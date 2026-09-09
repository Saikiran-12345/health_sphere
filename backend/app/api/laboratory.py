from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.laboratory import LabTest, LabOrder

router = APIRouter(prefix="/api/laboratory", tags=["Laboratory"])

@router.get("/tests")
def get_tests(db: Session = Depends(get_db)):
    return db.query(LabTest).all()
