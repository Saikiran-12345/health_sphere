from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.patient import Patient
from app.services.reporting import ReportingService
from app.api.deps import get_current_active_admin

router = APIRouter(prefix="/api/export", tags=["Data Export"])

@router.get("/patients/csv")
def export_patients_csv(db: Session = Depends(get_db), current_user = Depends(get_current_active_admin)):
    patients = db.query(Patient).all()
    if not patients:
        raise HTTPException(status_code=404, detail="No patients found")
        
    data = []
    for p in patients:
        data.append({
            "id": str(p.id),
            "date_of_birth": p.date_of_birth.isoformat(),
            "gender": p.gender,
            "blood_group": p.blood_group.value if p.blood_group else ""
        })
        
    csv_str = ReportingService.generate_csv_report(["id", "date_of_birth", "gender", "blood_group"], data)
    
    return StreamingResponse(
        iter([csv_str]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=patients_export.csv"}
    )
