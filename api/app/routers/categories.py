"""
Categories router - API endpoints for category management.

This module handles all HTTP requests for category operations:
- GET /api/v1/categories - List all categories
- POST /api/v1/categories - Create a new category
- GET /api/v1/categories/{id} - Get a specific category
- PUT /api/v1/categories/{id} - Update a category
- DELETE /api/v1/categories/{id} - Delete a category

Each endpoint uses:
- Pydantic schemas for validation
- CRUD functions for database operations
- Dependency injection for database sessions
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import Category, CategoryCreate, CategoryUpdate
from app.crud import (
    get_category,
    get_categories,
    get_categories_by_type,
    create_category,
    update_category,
    delete_category
)

# Create router instance
router = APIRouter()


@router.get("/", response_model=List[Category])
def list_categories(
    skip: int = 0,
    limit: int = 100,
    type: str = None,
    db: Session = Depends(get_db)
):
    """
    Get all categories with optional filtering.

    Query Parameters:
        - skip: Number of records to skip (default: 0)
        - limit: Maximum records to return (default: 100)
        - type: Filter by type ("income" or "expense")

    Returns:
        List of categories

    Example:
        GET /api/v1/categories
        GET /api/v1/categories?type=expense
        GET /api/v1/categories?skip=10&limit=20
    """
    if type:
        # Filter by type if provided
        return get_categories_by_type(db, type)
    else:
        # Get all categories with pagination
        return get_categories(db, skip=skip, limit=limit)


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_new_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new category.

    Request Body:
        {
            "name": "Food",
            "type": "expense",
            "color": "#FF5733",
            "icon": "🍔"
        }

    Returns:
        Created category with generated ID

    Status Codes:
        - 201: Category created successfully
        - 422: Validation error (invalid data)
    """
    return create_category(db, category)


@router.get("/{category_id}", response_model=Category)
def get_category_by_id(
    category_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific category by ID.

    Path Parameters:
        - category_id: ID of the category

    Returns:
        Category object

    Status Codes:
        - 200: Category found
        - 404: Category not found

    Example:
        GET /api/v1/categories/1
    """
    db_category = get_category(db, category_id)

    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )

    return db_category


@router.put("/{category_id}", response_model=Category)
def update_existing_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing category.

    Path Parameters:
        - category_id: ID of the category to update

    Request Body (all fields optional):
        {
            "name": "Groceries",
            "color": "#00FF00"
        }

    Returns:
        Updated category

    Status Codes:
        - 200: Category updated successfully
        - 404: Category not found
        - 422: Validation error

    Example:
        PUT /api/v1/categories/1
    """
    db_category = update_category(db, category_id, category)

    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )

    return db_category


@router.delete("/{category_id}", response_model=Category)
def delete_existing_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a category.

    Path Parameters:
        - category_id: ID of the category to delete

    Returns:
        Deleted category

    Status Codes:
        - 200: Category deleted successfully
        - 404: Category not found

    Warning:
        This will also delete all transactions in this category
        due to cascade delete.

    Example:
        DELETE /api/v1/categories/1
    """
    db_category = delete_category(db, category_id)

    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )

    return db_category
