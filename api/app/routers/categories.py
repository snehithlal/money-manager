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
from app.schemas.category import Category, CategoryCreate, CategoryUpdate
from app import crud
from app.api.deps import get_current_user
from app.models.user import User

# Create router instance
router = APIRouter()


@router.get("/", response_model=List[Category])
def list_categories(
    skip: int = 0,
    limit: int = 100,
    type: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get all categories for the current user with optional filtering.

    Query Parameters:
        - skip: Number of records to skip (default: 0)
        - limit: Maximum records to return (default: 100)
        - type: Filter by type ("income" or "expense")

    Returns:
        List of categories
    """
    if type:
        return crud.get_categories_by_type(db, type=type, user_id=current_user.id)
    return crud.get_categories(db, skip=skip, limit=limit, user_id=current_user.id)


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new category for the current user.

    Request Body:
        {
            "name": "Food",
            "type": "expense",
            "color": "#FF5733",
            "icon": "🍔"
        }

    Returns:
        Created category with generated ID
    """
    return crud.create_category(db=db, category=category, user_id=current_user.id)


@router.get("/{category_id}", response_model=Category)
def read_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get a specific category by ID (must belong to current user).

    Path Parameters:
        - category_id: ID of the category

    Returns:
        Category object
    """
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None or db_category.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.put("/{category_id}", response_model=Category)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update an existing category (must belong to current user).

    Path Parameters:
        - category_id: ID of the category to update

    Request Body (all fields optional):
        {
            "name": "Groceries",
            "color": "#00FF00"
        }

    Returns:
        Updated category
    """
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None or db_category.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.update_category(db=db, category_id=category_id, category=category, user_id=current_user.id)


@router.delete("/{category_id}", response_model=Category)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a category (must belong to current user).

    Path Parameters:
        - category_id: ID of the category to delete

    Returns:
        Deleted category
    """
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None or db_category.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.delete_category(db=db, category_id=category_id, user_id=current_user.id)
