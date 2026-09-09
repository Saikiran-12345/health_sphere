from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.dietary import DietPlan, MealOrder

router = APIRouter(prefix="/api/dietary", tags=["Dietary & Kitchen"])

@router.get("/plans")
def get_diet_plans(db: Session = Depends(get_db)):
    return db.query(DietPlan).all()
