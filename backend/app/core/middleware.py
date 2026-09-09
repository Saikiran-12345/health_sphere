import time
import uuid
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

# Setup basic logger for audit trail
logger = logging.getLogger("audit_logger")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("audit_access.log")
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

class AdvancedAuditMiddleware(BaseHTTPMiddleware):
    """
    HIPAA-compliant middleware to trace all API requests, execution time, and client IP.
    """
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        request_id = str(uuid.uuid4())
        
        # Extract Client Info
        client_ip = request.client.host if request.client else "Unknown"
        method = request.method
        url = request.url.path
        
        logger.info(f"REQ [{request_id}] | IP: {client_ip} | {method} {url}")
        
        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            logger.info(f"RES [{request_id}] | Status: {response.status_code} | Time: {process_time:.4f}s")
            
            # Inject security and tracing headers
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time"] = str(process_time)
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
            response.headers["X-Content-Type-Options"] = "nosniff"
            
            return response
            
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(f"ERR [{request_id}] | Exception: {str(e)} | Time: {process_time:.4f}s")
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error", "request_id": request_id}
            )

class SimpleRateLimiterMiddleware(BaseHTTPMiddleware):
    """
    In-memory rate limiter to prevent abuse (DDoS mitigation).
    Note: For true enterprise, use Redis.
    """
    def __init__(self, app, max_requests: int = 100, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.ip_records = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "Unknown"
        current_time = time.time()
        
        # Clean old records
        if client_ip in self.ip_records:
            self.ip_records[client_ip] = [t for t in self.ip_records[client_ip] if current_time - t < self.window_seconds]
        else:
            self.ip_records[client_ip] = []
            
        if len(self.ip_records[client_ip]) >= self.max_requests:
            return JSONResponse(
                status_code=429,
                content={"detail": "Too Many Requests. Please slow down."}
            )
            
        self.ip_records[client_ip].append(current_time)
        return await call_next(request)
