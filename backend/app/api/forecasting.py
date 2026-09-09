from fastapi import APIRouter, Depends
from app.services.forecasting import SupplyChainForecaster

router = APIRouter(prefix="/api/forecast", tags=["Supply Chain AI"])

@router.get("/medicine/{name}")
def get_medicine_forecast(name: str):
    return SupplyChainForecaster.forecast_demand(name)
