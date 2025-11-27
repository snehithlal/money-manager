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
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/monthly/{year}/{month}", response_model=MonthlySummary)
def read_monthly_summary(
    year: int,
    month: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get financial summary (income, expense, balance) for a specific month (current user).
    """
    return crud.get_monthly_summary(db, year=year, month=month, user_id=current_user.id)

@router.get("/categories", response_model=List[CategorySummary])
def read_category_summary(
    type: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get spending/income breakdown by category (current user).
    Optional 'type' query param: 'income' or 'expense'.
    """
    return crud.get_category_summary(db, type=type, user_id=current_user.id)
