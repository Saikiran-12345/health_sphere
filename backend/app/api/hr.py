from fastapi import APIRouter
router = APIRouter(prefix="/api/hr", tags=["HR & Payroll"])

@router.get("/payroll")
def get_payroll():
    return []
