"""
User Pydantic schemas.

These schemas define the structure of data for user-related API requests and responses.
"""

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """Base schema for User data"""
    email: EmailStr

class UserCreate(UserBase):
    """Schema for creating a new user (registration)"""
    password: str

class User(UserBase):
    """Schema for returning user data"""
    id: int
    is_active: bool

    class Config:
        from_attributes = True
