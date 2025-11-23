"""
Analytics Pydantic schemas.

These schemas define the structure of data for analytics-related API responses.
"""

from pydantic import BaseModel, Field


class MonthlySummary(BaseModel):
    """Schema for monthly income/expense summary"""
    month: str = Field(..., description="Month in YYYY-MM format")
    total_income: float
    total_expense: float
    balance: float


class CategorySummary(BaseModel):
    """Schema for spending by category"""
    category_id: int
    category_name: str
    category_color: str
    category_icon: str
    total_amount: float
    transaction_count: int
