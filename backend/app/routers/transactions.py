"""
Transactions router - API endpoints for transaction management.

This module handles all HTTP requests for transaction operations:
- GET /api/v1/transactions - List all transactions (with filters)
- POST /api/v1/transactions - Create a new transaction
- GET /api/v1/transactions/{id} - Get a specific transaction
- PUT /api/v1/transactions/{id} - Update a transaction
- DELETE /api/v1/transactions/{id} - Delete a transaction

Features:
- Advanced filtering (by type, category, date range)
- Pagination support
- Nested category information in responses
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.database import get_db
from app.schemas import Transaction, TransactionCreate, TransactionUpdate
from app import crud
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("", response_model=List[Transaction])
def list_transactions(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum records to return"),
    type: Optional[str] = Query(None, description="Filter by type: income or expense"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    start_date: Optional[date] = Query(None, description="Filter from this date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="Filter until this date (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get all transactions for the current user with optional filtering.

    Query Parameters:
        - skip: Number of records to skip (default: 0)
        - limit: Maximum records to return (default: 100, max: 1000)
        - type: Filter by "income" or "expense"
        - category_id: Filter by category ID
        - start_date: Filter transactions from this date
        - end_date: Filter transactions until this date

    Returns:
        List of transactions with nested category information
    """
    return crud.get_transactions(
        db,
        skip=skip,
        limit=limit,
        type=type,
        category_id=category_id,
        start_date=start_date,
        end_date=end_date,
        user_id=current_user.id
    )


@router.post("", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new transaction for the current user.

    Request Body:
        {
            "amount": 50.00,
            "description": "Groceries at Whole Foods",
            "date": "2024-01-15",
            "category_id": 1,
            "type": "expense"
        }

    Returns:
        Created transaction with generated ID and category info
    """
    # Verify category belongs to user
    category = crud.get_category(db, category_id=transaction.category_id)
    if not category or category.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Invalid category")

    return crud.create_transaction(db, transaction, user_id=current_user.id)


@router.get("/{transaction_id}", response_model=Transaction)
def read_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get a specific transaction by ID (must belong to current user).

    Path Parameters:
        - transaction_id: ID of the transaction

    Returns:
        Transaction object with nested category information
    """
    db_transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None or db_transaction.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


@router.put("/{transaction_id}", response_model=Transaction)
def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update a transaction (must belong to current user).

    Path Parameters:
        - transaction_id: ID of the transaction to update

    Returns:
        Updated transaction
    """
    db_transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None or db_transaction.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return crud.update_transaction(db=db, transaction_id=transaction_id, transaction=transaction, user_id=current_user.id)


@router.delete("/{transaction_id}", response_model=Transaction)
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a transaction (must belong to current user).

    Path Parameters:
        - transaction_id: ID of the transaction to delete

    Returns:
        Deleted transaction
    """
    db_transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None or db_transaction.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return crud.delete_transaction(db=db, transaction_id=transaction_id, user_id=current_user.id)
