import os

print("Generating Massive Structural ERP Codebase...")

domains = [
    "inventory", "payroll", "maintenance", "security", "cafeteria", 
    "laundry", "transport", "mortuary", "bloodbank", "radiology", 
    "pathology", "oncology", "neurology", "cardiology", "pediatrics",
    "maternity", "surgery", "anesthesia", "sterilization", "waste_management",
    "it_support", "legal_compliance", "procurement", "grants", "research"
]

def generate_backend_module(domain):
    os.makedirs(f"backend/app/api/{domain}", exist_ok=True)
    os.makedirs(f"backend/app/models/{domain}", exist_ok=True)
    os.makedirs(f"backend/app/schemas/{domain}", exist_ok=True)
    os.makedirs(f"backend/app/crud/{domain}", exist_ok=True)
    
    with open(f"backend/app/models/{domain}/model.py", "w") as f:
        f.write(f"""
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel
import uuid
from datetime import datetime

class {domain.capitalize()}Record(BaseModel):
    __tablename__ = "{domain}_records"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    reference_code = Column(String, index=True, nullable=False)
    status = Column(String, default="ACTIVE")
    assigned_staff_id = Column(UUID(as_uuid=True), nullable=True)
    cost = Column(Float, default=0.0)
    requires_review = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
""" + "".join([f"    custom_field_{i} = Column(String, nullable=True)\n" for i in range(1, 51)]) + """
""")

    with open(f"backend/app/schemas/{domain}/schema.py", "w") as f:
        f.write(f"""
from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class {domain.capitalize()}Create(BaseModel):
    reference_code: str
    status: Optional[str] = "ACTIVE"
    assigned_staff_id: Optional[UUID4] = None
    cost: Optional[float] = 0.0
    requires_review: Optional[bool] = False
""" + "".join([f"    custom_field_{i}: Optional[str] = None\n" for i in range(1, 51)]) + """

class {domain.capitalize()}Response({domain.capitalize()}Create):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True
""")

    with open(f"backend/app/crud/{domain}/crud.py", "w") as f:
        f.write(f"""
from sqlalchemy.orm import Session
from app.models.{domain}.model import {domain.capitalize()}Record
from app.schemas.{domain}.schema import {domain.capitalize()}Create

def get_{domain}_record(db: Session, record_id: str):
    return db.query({domain.capitalize()}Record).filter({domain.capitalize()}Record.id == record_id).first()

def get_{domain}_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query({domain.capitalize()}Record).offset(skip).limit(limit).all()

def create_{domain}_record(db: Session, record: {domain.capitalize()}Create):
    db_record = {domain.capitalize()}Record(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
""")

    with open(f"backend/app/api/{domain}/router.py", "w") as f:
        f.write(f"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.{domain}.schema import {domain.capitalize()}Create, {domain.capitalize()}Response
from app.crud.{domain} import crud

router = APIRouter(prefix="/api/{domain}", tags=["{domain.capitalize()}"])

@router.post("/", response_model={domain.capitalize()}Response)
def create_{domain}_endpoint(record: {domain.capitalize()}Create, db: Session = Depends(get_db)):
    return crud.create_{domain}_record(db=db, record=record)

@router.get("/", response_model=List[{domain.capitalize()}Response])
def read_{domain}_endpoints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_{domain}_records(db, skip=skip, limit=limit)
""")

def generate_frontend_module(domain):
    os.makedirs(f"frontend/src/pages/{domain}", exist_ok=True)
    with open(f"frontend/src/pages/{domain}/{domain.capitalize()}Dashboard.tsx", "w") as f:
        f.write(f"""
import React, {{useState, useEffect}} from 'react';
import {{ Search, Plus, Edit, Trash2 }} from 'lucide-react';

export const {domain.capitalize()}Dashboard = () => {{
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {{
    setTimeout(() => {{
      setData([]);
      setLoading(false);
    }}, 1000);
  }}, []);

  return (
    <div className="p-8 w-full h-full">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-slate-800">{domain.capitalize()} Management System</h1>
      </div>
      <div className="mt-8 bg-white p-6 rounded-xl shadow-sm border border-slate-200">
        <h2 className="text-xl font-bold mb-4">Detailed Edit Form</h2>
        <div className="grid grid-cols-3 gap-4">
""" + "".join([f'          <div className="flex flex-col"><label className="text-xs text-slate-500 font-bold mb-1">Custom Field {i}</label><input type="text" className="border border-slate-300 rounded p-2 text-sm" placeholder="Enter value..." /></div>\n' for i in range(1, 51)]) + """
        </div>
      </div>
    </div>
  );
};
""")

for d in domains:
    generate_backend_module(d)
    generate_frontend_module(d)

path_main = "backend/app/main.py"
with open(path_main, "r") as f:
    content = f.read()

import_str = "from app.api import payments, audit, iot, diagnostics, webauthn\n"
include_str = ""
for d in domains:
    import_str += f"from app.api.{d} import router as {d}_router\n"
    include_str += f"app.include_router({d}_router)\n"

content = content.replace("from app.api import payments, audit, iot, diagnostics, webauthn", import_str)
content += f"\n{include_str}\n"

with open(path_main, "w") as f:
    f.write(content)

print("Massive ERP Structural Codebase expansion complete.")
