"""
CRUD operations for Transaction model.

These functions handle all database operations for transactions.
"""

from sqlalchemy.orm import Session
from sqlalchemy import and_, extract
from datetime import date, datetime
from app.models import Transaction
from app.schemas import TransactionCreate, TransactionUpdate


def get_transaction(db: Session, transaction_id: int):
    """
    Get a single transaction by ID.

    Args:
        db: Database session
        transaction_id: ID of the transaction

    Returns:
        Transaction object or None
    """
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()


def get_transactions(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    transaction_type: str = None,
    category_id: int = None,
    start_date: date = None,
    end_date: date = None
):
    """
    Get transactions with optional filtering, scoped to user.

    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum records to return
        transaction_type: Filter by type ("income" or "expense")
        category_id: Filter by category ID
        start_date: Filter transactions from this date
        end_date: Filter transactions until this date
        user_id: ID of the user

    Returns:
        List of Transaction objects
    """
    query = db.query(Transaction).filter(Transaction.user_id == user_id)

    # Apply filters if provided
    if transaction_type:
        query = query.filter(Transaction.type == transaction_type)

    if category_id:
        query = query.filter(Transaction.category_id == category_id)

    if start_date:
        query = query.filter(Transaction.date >= start_date)

    if end_date:
        query = query.filter(Transaction.date <= end_date)

    # Order by date (newest first) and apply pagination
    return query.order_by(Transaction.date.desc()).offset(skip).limit(limit).all()


def get_transactions_by_month(db: Session, year: int, month: int, user_id: int):
    """
    Get all transactions for a specific month and user.

    Args:
        db: Database session
        year: Year (e.g., 2024)
        month: Month (1-12)
        user_id: ID of the user

    Returns:
        List of Transaction objects
    """
    return db.query(Transaction).filter(
        and_(
            extract('year', Transaction.date) == year,
            extract('month', Transaction.date) == month,
            Transaction.user_id == user_id
        )
    ).order_by(Transaction.date.desc()).all()


def create_transaction(db: Session, transaction: TransactionCreate, user_id: int):
    """
    Create a new transaction for a user.

    Args:
        db: Database session
        transaction: TransactionCreate schema
        user_id: ID of the user creating the transaction

    Returns:
        Created Transaction object
    """
    db_transaction = Transaction(**transaction.model_dump(), user_id=user_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def update_transaction(db: Session, transaction_id: int, transaction: TransactionUpdate, user_id: int):
    """
    Update an existing transaction, scoped to user.

    Args:
        db: Database session
        transaction_id: ID of transaction to update
        transaction: TransactionUpdate schema
        user_id: ID of the user who owns the transaction

    Returns:
        Updated Transaction object or None
    """
    db_transaction = get_transaction(db, transaction_id, user_id)

    if db_transaction is None:
        return None

    # Update only provided fields
    update_data = transaction.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_transaction, field, value)

    db.commit()
    db.refresh(db_transaction)

    return db_transaction


def delete_transaction(db: Session, transaction_id: int, user_id: int):
    """
    Delete a transaction, scoped to user.

    Args:
        db: Database session
        transaction_id: ID of transaction to delete
        user_id: ID of the user who owns the transaction

    Returns:
        Deleted Transaction object or None
    """
    db_transaction = get_transaction(db, transaction_id, user_id)

    if db_transaction is None:
        return None

    db.delete(db_transaction)
    db.commit()

    return db_transaction
