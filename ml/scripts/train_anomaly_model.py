import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

def train_anomaly_detection():
    print("Training Operational Anomaly Detection (Isolation Forest)...")
    # Synthetic operational metrics: [daily_appointments, cancellations, inventory_usage]
    np.random.seed(42)
    normal_data = np.random.normal(loc=[100, 5, 50], scale=[10, 2, 5], size=(1000, 3))
    anomalies = np.random.normal(loc=[200, 30, 150], scale=[20, 5, 20], size=(50, 3))
    
    X = np.vstack([normal_data, anomalies])
    
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    
    os.makedirs('../models', exist_ok=True)
    joblib.dump(model, '../models/operational_anomaly_model.joblib')
    print("Anomaly model saved to ml/models/operational_anomaly_model.joblib")

if __name__ == "__main__":
    train_anomaly_detection()
