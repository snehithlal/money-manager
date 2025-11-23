from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.models.transaction import Transaction
from app.models.category import Category
from app.schemas.analytics import MonthlySummary, CategorySummary
from datetime import date
import calendar

def get_monthly_summary(db: Session, year: int, month: int) -> MonthlySummary:
    """
    Calculate total income, expense, and balance for a specific month.
    """
    # Get start and end date of the month
    start_date = date(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end_date = date(year, month, last_day)

    # Query to sum amounts by type
    results = db.query(
        Transaction.type,
        func.sum(Transaction.amount).label("total")
    ).filter(
        Transaction.date >= start_date,
        Transaction.date <= end_date
    ).group_by(Transaction.type).all()

    total_income = 0.0
    total_expense = 0.0

    for r in results:
        if r.type == "income":
            total_income = float(r.total or 0)
        elif r.type == "expense":
            total_expense = float(r.total or 0)

    return MonthlySummary(
        month=f"{year}-{month:02d}",
        total_income=total_income,
        total_expense=total_expense,
        balance=total_income - total_expense
    )

def get_category_summary(db: Session, type: str = None) -> list[CategorySummary]:
    """
    Calculate total amount per category, optionally filtered by transaction type.
    """
    query = db.query(
        Category.name,
        Category.color,
        Category.icon,
        func.sum(Transaction.amount).label("total")
    ).join(Transaction).group_by(Category.id)

    if type:
        query = query.filter(Transaction.type == type)

    results = query.all()

    summary = []
    for r in results:
        summary.append(CategorySummary(
            category_name=r.name,
            total_amount=float(r.total or 0),
            color=r.color,
            icon=r.icon
        ))

    # Sort by total amount descending
    summary.sort(key=lambda x: x.total_amount, reverse=True)

    return summary
