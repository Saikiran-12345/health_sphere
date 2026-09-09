from typing import List
from fastapi import HTTPException, Security, Depends
from app.models.user import UserRole, User
from app.api.deps import get_current_user

class RoleChecker:
    """
    Granular Role-Based Access Control (RBAC) dependency.
    Allows specifying required roles for specific endpoints.
    """
    def __init__(self, allowed_roles: List[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Security(get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=403,
                detail=f"Operation not permitted. Required one of: {[r.name for r in self.allowed_roles]}"
            )
        return user
