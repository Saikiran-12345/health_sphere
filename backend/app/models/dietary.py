from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class DietPlan(BaseModel):
    __tablename__ = "diet_plans"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    dietitian_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    plan_name = Column(String(100), nullable=False) # DIABETIC, RENAL, LIQUID, REGULAR
    restrictions = Column(Text, nullable=True)
    active = Column(String(50), default="ACTIVE")

class MealOrder(BaseModel):
    __tablename__ = "meal_orders"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    bed_id = Column(UUID(as_uuid=True), ForeignKey("beds.id"), nullable=False)
    diet_plan_id = Column(UUID(as_uuid=True), ForeignKey("diet_plans.id"), nullable=True)
    meal_type = Column(String(50), nullable=False) # BREAKFAST, LUNCH, DINNER
    delivery_time = Column(DateTime, nullable=False)
    status = Column(String(50), default="PREPARING") # PREPARING, DELIVERED
