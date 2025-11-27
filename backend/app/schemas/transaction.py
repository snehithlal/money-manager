"""
Transaction Pydantic schemas.

These schemas define the structure of data for transaction-related API requests and responses.
"""

from pydantic import BaseModel, Field
from datetime import date as datetime_date
from typing import Optional
from .category import TransactionType, Category


class TransactionBase(BaseModel):
    """Base schema with common transaction fields"""
    amount: float = Field(..., gt=0, description="Transaction amount (must be positive)")
    description: Optional[str] = Field(None, max_length=200, description="Optional description")
    date: datetime_date = Field(..., description="Transaction date")
    category_id: int = Field(..., gt=0, description="Category ID")
    type: TransactionType = Field(..., description="Transaction type: income or expense")


class TransactionCreate(TransactionBase):
    """Schema for creating a new transaction"""
    pass


class TransactionUpdate(BaseModel):
    """Schema for updating a transaction (all fields optional)"""
    amount: Optional[float] = Field(None, gt=0)
    description: Optional[str] = Field(None, max_length=200)
    date: Optional[datetime_date] = None
    category_id: Optional[int] = Field(None, gt=0)
    type: Optional[TransactionType] = None


class Transaction(TransactionBase):
    """Schema for transaction responses (includes database ID and category)"""
    id: int
    category: Category  # Nested category information

    class Config:
        from_attributes = True
