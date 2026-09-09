import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Any

class SupplyChainForecaster:
    @staticmethod
    def forecast_demand(medicine_name: str, historical_days: int = 90) -> Dict[str, Any]:
        """
        Simulates an ARIMA or Prophet time-series forecast for medicine consumption.
        """
        # Generate synthetic historical consumption data
        np.random.seed(len(medicine_name))
        base_consumption = np.random.randint(5, 50)
        trend = np.linspace(0, 5, historical_days)
        noise = np.random.normal(0, 2, historical_days)
        
        historical = base_consumption + trend + noise
        
        # Forecast next 30 days based on moving average + exponential smoothing mock
        recent_avg = np.mean(historical[-14:])
        projected_daily = recent_avg * 1.05  # Assume 5% growth
        
        forecast_30_days = int(projected_daily * 30)
        
        return {
            "medicine": medicine_name,
            "historical_average_daily": float(np.mean(historical)),
            "projected_30_day_demand": forecast_30_days,
            "confidence_interval_lower": int(forecast_30_days * 0.85),
            "confidence_interval_upper": int(forecast_30_days * 1.15),
            "recommendation": "URGENT_REORDER" if forecast_30_days > 200 else "STOCK_SUFFICIENT"
        }
