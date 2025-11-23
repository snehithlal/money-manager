"""
Analytics router - API endpoints for financial analytics.

This will handle:
- GET /api/analytics/monthly - Monthly income/expense summary
- GET /api/analytics/by-category - Spending by category
- GET /api/analytics/trends - Historical trends
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud
from app.schemas.analytics import MonthlySummary, CategorySummary

router = APIRouter()

@router.get("/monthly/{year}/{month}", response_model=MonthlySummary)
def read_monthly_summary(
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    """
    Get financial summary (income, expense, balance) for a specific month.
    """
    return crud.get_monthly_summary(db, year=year, month=month)

@router.get("/categories", response_model=List[CategorySummary])
def read_category_summary(
    type: str = None,
    db: Session = Depends(get_db)
):
    """
    Get spending/income breakdown by category.
    Optional 'type' query param: 'income' or 'expense'.
    """
    return crud.get_category_summary(db, type=type)
