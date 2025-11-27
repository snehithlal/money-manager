"""
Token Pydantic schemas.

These schemas define the structure of JWT tokens.
"""

from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Schema for JWT token payload"""
    email: Optional[str] = None
