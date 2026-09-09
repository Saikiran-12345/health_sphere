import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Advanced RBAC Dependency
create_file('backend/app/core/rbac.py', """
from typing import List
from fastapi import HTTPException, Security, Depends
from app.models.user import UserRole, User
from app.api.deps import get_current_user

class RoleChecker:
    \"\"\"
    Granular Role-Based Access Control (RBAC) dependency.
    Allows specifying required roles for specific endpoints.
    \"\"\"
    def __init__(self, allowed_roles: List[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Security(get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=403,
                detail=f"Operation not permitted. Required one of: {[r.name for r in self.allowed_roles]}"
            )
        return user
""")

# 2. Advanced Security & Audit Middleware
create_file('backend/app/core/middleware.py', """
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
    \"\"\"
    HIPAA-compliant middleware to trace all API requests, execution time, and client IP.
    \"\"\"
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
    \"\"\"
    In-memory rate limiter to prevent abuse (DDoS mitigation).
    Note: For true enterprise, use Redis.
    \"\"\"
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
""")

# 3. Attach Middlewares to Main
path_main = "backend/app/main.py"
with open(path_main, "r") as f:
    content = f.read()

if "from app.core.middleware import AdvancedAuditMiddleware" not in content:
    # Add imports
    content = content.replace(
        "from fastapi import FastAPI", 
        "from fastapi import FastAPI\nfrom app.core.middleware import AdvancedAuditMiddleware, SimpleRateLimiterMiddleware"
    )
    # Add middlewares (order matters, put them after app initialization)
    app_init = 'app = FastAPI(title="HealthSphere Enterprise API")'
    middleware_attachments = f'{app_init}\n\napp.add_middleware(SimpleRateLimiterMiddleware, max_requests=100, window_seconds=60)\napp.add_middleware(AdvancedAuditMiddleware)\n'
    content = content.replace(app_init, middleware_attachments)
    
    with open(path_main, "w") as f:
        f.write(content)

# 4. Apply RBAC to a sensitive route (e.g. Telemedicine)
path_tele = "backend/app/api/telemedicine.py"
with open(path_tele, "r") as f:
    tele_content = f.read()

if "RoleChecker" not in tele_content:
    tele_content = tele_content.replace(
        "from fastapi import APIRouter, WebSocket, WebSocketDisconnect",
        "from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends\nfrom app.core.rbac import RoleChecker\nfrom app.models.user import UserRole"
    )
    tele_content = tele_content.replace(
        'router = APIRouter(prefix="/api/telemedicine", tags=["Telemedicine"])',
        'allow_doctors_only = RoleChecker([UserRole.DOCTOR, UserRole.ADMIN])\n\nrouter = APIRouter(prefix="/api/telemedicine", tags=["Telemedicine"], dependencies=[Depends(allow_doctors_only)])'
    )
    with open(path_tele, "w") as f:
        f.write(tele_content)

print("Advanced RBAC and Middlewares generated.")
