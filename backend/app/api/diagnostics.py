from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from app.services.xray_ml_engine import XRayAnalyzer
from app.api.deps import get_current_user

router = APIRouter(prefix="/api/diagnostics", tags=["ML Diagnostics"])

@router.post("/xray/analyze")
async def analyze_xray(file: UploadFile = File(...), current_user = Depends(get_current_user)):
    """
    Upload a Chest X-Ray (JPEG/PNG) and instantly receive an AI-driven diagnosis.
    """
    if not file.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Only PNG and JPEG formats are supported.")
        
    image_bytes = await file.read()
    
    # Run the ML engine
    results = XRayAnalyzer.analyze_scan(image_bytes)
    
    if "error" in results:
        raise HTTPException(status_code=500, detail=results["error"])
        
    return {
        "filename": file.filename,
        "analyzed_by_ai": True,
        "results": results
    }
