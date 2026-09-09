import cv2
import numpy as np
import logging
import base64

logger = logging.getLogger(__name__)

class XRayAnalyzer:
    """
    Computer Vision engine designed to analyze Chest X-Rays for signs of Pneumonia.
    (This is a simulated ML pipeline using OpenCV contour analysis for demonstration).
    """
    
    @staticmethod
    def analyze_scan(image_bytes: bytes) -> dict:
        try:
            # Decode the image bytes into an OpenCV matrix
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
            
            if img is None:
                raise ValueError("Could not decode image bytes")

            # Apply Gaussian Blur to reduce noise
            blurred = cv2.GaussianBlur(img, (5, 5), 0)
            
            # Edge detection to simulate finding lung opacities
            edges = cv2.Canny(blurred, 50, 150)
            
            # Count dense regions (simulating opacity measurement)
            dense_pixels = np.sum(edges == 255)
            total_pixels = img.shape[0] * img.shape[1]
            opacity_ratio = dense_pixels / total_pixels
            
            # Generate a risk score based on opacity density
            risk_score = min(max(opacity_ratio * 1000, 0), 100)
            
            diagnosis = "NORMAL"
            confidence = 0.95
            
            if risk_score > 65:
                diagnosis = "SEVERE PNEUMONIA DETECTED"
                confidence = 0.89
            elif risk_score > 40:
                diagnosis = "MILD OPACITY (MONITOR)"
                confidence = 0.82
                
            return {
                "diagnosis": diagnosis,
                "confidence_score": confidence,
                "opacity_ratio": round(opacity_ratio, 4),
                "risk_index": round(risk_score, 2),
                "requires_human_review": risk_score > 40
            }
            
        except Exception as e:
            logger.error(f"X-Ray Analysis Failed: {str(e)}")
            return {"error": "Machine Learning inference failed. Please request human review."}
