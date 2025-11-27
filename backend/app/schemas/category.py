"""
Category Pydantic schemas.

These schemas define the structure of data for category-related API requests and responses.
They provide automatic validation and documentation.
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class TransactionType(str, Enum):
    """Transaction type enum"""
    INCOME = "income"
    EXPENSE = "expense"


class CategoryBase(BaseModel):
    """Base schema with common category fields"""
    name: str = Field(..., min_length=1, max_length=50, description="Category name")
    type: TransactionType = Field(..., description="Category type: income or expense")
    color: str = Field(default="#6366f1", pattern="^#[0-9A-Fa-f]{6}$", description="Hex color code")
    icon: str = Field(default="💰", max_length=10, description="Icon or emoji")


class CategoryCreate(CategoryBase):
    """Schema for creating a new category"""
    pass


class CategoryUpdate(BaseModel):
    """Schema for updating a category (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    type: Optional[TransactionType] = None
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")
    icon: Optional[str] = Field(None, max_length=10)


class Category(CategoryBase):
    """Schema for category responses (includes database ID)"""
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to work with SQLAlchemy models
