from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.security import SECRET_KEY, ALGORITHM
from app.models.user import User
from app.schemas.user import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("id")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(id=user_id, role=payload.get("role"))
    except JWTError:
        raise credentials_exception
        
    user = db.query(User).filter(User.id == token_data.id).first()
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user

def get_current_active_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role.value != "ADMIN":
        raise HTTPException(status_code=403, detail="Not enough privileges")
    return current_user

def get_current_doctor(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role.value not in ["ADMIN", "DOCTOR"]:
        raise HTTPException(status_code=403, detail="Doctor privileges required")
    return current_user
