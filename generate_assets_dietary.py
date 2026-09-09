import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Asset Management (Models, API)
create_file('backend/app/models/assets.py', """
from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Asset(BaseModel):
    __tablename__ = "assets"
    name = Column(String(255), nullable=False)
    serial_number = Column(String(100), unique=True, nullable=False)
    category = Column(String(100), nullable=False) # IMAGING, SURGICAL, TRANSPORT, IT
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=True)
    purchase_date = Column(DateTime, nullable=False)
    last_maintenance = Column(DateTime, nullable=True)
    status = Column(String(50), default="OPERATIONAL") # OPERATIONAL, MAINTENANCE, DECOMMISSIONED

class MaintenanceLog(BaseModel):
    __tablename__ = "maintenance_logs"
    asset_id = Column(UUID(as_uuid=True), ForeignKey("assets.id"), nullable=False)
    technician = Column(String(100), nullable=False)
    issue_description = Column(String(500), nullable=False)
    resolution = Column(String(500), nullable=True)
    cost = Column(Float, default=0.0)
    date_logged = Column(DateTime, nullable=False)
""")

create_file('backend/app/api/assets.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.assets import Asset, MaintenanceLog

router = APIRouter(prefix="/api/assets", tags=["Asset & Maintenance Management"])

@router.get("/")
def get_assets(db: Session = Depends(get_db)):
    return db.query(Asset).all()

@router.get("/{asset_id}/logs")
def get_maintenance_logs(asset_id: str, db: Session = Depends(get_db)):
    return db.query(MaintenanceLog).filter(MaintenanceLog.asset_id == asset_id).all()
""")

# 2. Dietary & Kitchen Management
create_file('backend/app/models/dietary.py', """
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
""")

create_file('backend/app/api/dietary.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.dietary import DietPlan, MealOrder

router = APIRouter(prefix="/api/dietary", tags=["Dietary & Kitchen"])

@router.get("/plans")
def get_diet_plans(db: Session = Depends(get_db)):
    return db.query(DietPlan).all()
""")

# Update main.py and __init__.py
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import assets" not in content:
    content = content.replace("from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance, telemedicine, export, forecasting", 
                              "from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance, telemedicine, export, forecasting, assets, dietary")
    content += "\napp.include_router(assets.router)\napp.include_router(dietary.router)\n"
    with open(path, "w") as f:
        f.write(content)

path2 = "backend/app/models/__init__.py"
with open(path2, "a") as f:
    f.write("\nfrom app.models.assets import Asset, MaintenanceLog\n")
    f.write("from app.models.dietary import DietPlan, MealOrder\n")

print("Assets and Dietary domains generated.")
