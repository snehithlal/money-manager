"""
API Dependencies.

Common dependencies used across API endpoints.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core import security
from app.database import get_db
from app.models.user import User
from app.schemas.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Dependency to get the current authenticated user from the JWT token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # print(f"DEBUG: Validating token: {token[:10]}...")
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            print("DEBUG: Token missing 'sub' (email)")
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError as e:
        print(f"DEBUG: JWT Error: {str(e)}")
        raise credentials_exception

    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        print(f"DEBUG: User not found for email: {token_data.email}")
        raise credentials_exception
    return user
