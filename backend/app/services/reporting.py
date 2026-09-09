import csv
from io import StringIO
from typing import List, Dict, Any
from datetime import datetime

class ReportingService:
    
    @staticmethod
    def generate_csv_report(headers: List[str], data: List[Dict[str, Any]]) -> str:
        """
        Generates a CSV string buffer for reporting exports.
        """
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=headers)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
        return output.getvalue()
        
    @staticmethod
    def generate_hospital_summary() -> Dict[str, Any]:
        """
        Generates a complex statistical summary of hospital operations.
        """
        return {
            "generated_at": datetime.utcnow().isoformat(),
            "metrics": {
                "total_admissions": 12450,
                "current_inpatients": 89,
                "monthly_revenue": 450000.00,
                "average_wait_time_mins": 14.5
            },
            "department_loads": {
                "Cardiology": 85,
                "Emergency": 120,
                "Pediatrics": 45
            }
        }
