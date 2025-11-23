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
from app.crud import (
    get_transaction,
    get_transactions,
    get_transactions_by_month,
    create_transaction,
    update_transaction,
    delete_transaction
)

router = APIRouter()


@router.get("/", response_model=List[Transaction])
def list_transactions(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum records to return"),
    type: Optional[str] = Query(None, description="Filter by type: income or expense"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    start_date: Optional[date] = Query(None, description="Filter from this date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="Filter until this date (YYYY-MM-DD)"),
    db: Session = Depends(get_db)
):
    """
    Get all transactions with optional filtering.

    Query Parameters:
        - skip: Number of records to skip (default: 0)
        - limit: Maximum records to return (default: 100, max: 1000)
        - type: Filter by "income" or "expense"
        - category_id: Filter by category ID
        - start_date: Filter transactions from this date
        - end_date: Filter transactions until this date

    Returns:
        List of transactions with nested category information

    Examples:
        GET /api/v1/transactions
        GET /api/v1/transactions?type=expense
        GET /api/v1/transactions?category_id=1
        GET /api/v1/transactions?start_date=2024-01-01&end_date=2024-01-31
        GET /api/v1/transactions?type=income&category_id=2&limit=50
    """
    return get_transactions(
        db,
        skip=skip,
        limit=limit,
        transaction_type=type,
        category_id=category_id,
        start_date=start_date,
        end_date=end_date
    )


@router.post("/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_new_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new transaction.

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

    Status Codes:
        - 201: Transaction created successfully
        - 422: Validation error (invalid data)
        - 404: Category not found (if category_id doesn't exist)

    Validation Rules:
        - amount: Must be positive number
        - description: Optional, max 200 characters
        - date: Required, format YYYY-MM-DD
        - category_id: Must exist in database
        - type: Must be "income" or "expense"
    """
    # Note: Foreign key constraint will raise error if category doesn't exist
    return create_transaction(db, transaction)


@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction_by_id(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific transaction by ID.

    Path Parameters:
        - transaction_id: ID of the transaction

    Returns:
        Transaction object with nested category information

    Status Codes:
        - 200: Transaction found
        - 404: Transaction not found

    Example:
        GET /api/v1/transactions/1
    """
    db_transaction = get_transaction(db, transaction_id)

    if db_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {transaction_id} not found"
        )

    return db_transaction


@router.put("/{transaction_id}", response_model=Transaction)
def update_existing_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing transaction.

    Path Parameters:
        - transaction_id: ID of the transaction to update

    Request Body (all fields optional):
        {
            "amount": 75.00,
            "description": "Updated description"
        }

    Returns:
        Updated transaction

    Status Codes:
        - 200: Transaction updated successfully
        - 404: Transaction not found
        - 422: Validation error

    Note:
        Only provided fields will be updated.
        Omitted fields will keep their current values.

    Example:
        PUT /api/v1/transactions/1
    """
    db_transaction = update_transaction(db, transaction_id, transaction)

    if db_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {transaction_id} not found"
        )

    return db_transaction


@router.delete("/{transaction_id}", response_model=Transaction)
def delete_existing_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a transaction.

    Path Parameters:
        - transaction_id: ID of the transaction to delete

    Returns:
        Deleted transaction

    Status Codes:
        - 200: Transaction deleted successfully
        - 404: Transaction not found

    Example:
        DELETE /api/v1/transactions/1
    """
    db_transaction = delete_transaction(db, transaction_id)

    if db_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {transaction_id} not found"
        )

    return db_transaction
