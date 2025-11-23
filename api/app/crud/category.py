"""
CRUD operations for Category model.

CRUD = Create, Read, Update, Delete
These functions handle all database operations for categories.

Each function takes a database session (db) and performs operations.
"""

from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate


def get_category(db: Session, category_id: int):
    """
    Get a single category by ID.

    Args:
        db: Database session
        category_id: ID of the category to retrieve

    Returns:
        Category object or None if not found
    """
    return db.query(Category).filter(Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    """
    Get all categories with pagination.

    Args:
        db: Database session
        skip: Number of records to skip (for pagination)
        limit: Maximum number of records to return

    Returns:
        List of Category objects
    """
    return db.query(Category).offset(skip).limit(limit).all()


def get_categories_by_type(db: Session, transaction_type: str):
    """
    Get categories filtered by type (income or expense).

    Args:
        db: Database session
        transaction_type: "income" or "expense"

    Returns:
        List of Category objects
    """
    return db.query(Category).filter(Category.type == transaction_type).all()


def create_category(db: Session, category: CategoryCreate):
    """
    Create a new category.

    Args:
        db: Database session
        category: CategoryCreate schema with category data

    Returns:
        Created Category object

    Process:
        1. Convert Pydantic schema to dict
        2. Create SQLAlchemy model instance
        3. Add to database session
        4. Commit transaction
        5. Refresh to get generated ID
        6. Return created category
    """
    # Convert Pydantic model to dict and create Category instance
    db_category = Category(**category.model_dump())

    # Add to session (stages the change)
    db.add(db_category)

    # Commit to database (executes INSERT)
    db.commit()

    # Refresh to get the generated ID and other defaults
    db.refresh(db_category)

    return db_category


def update_category(db: Session, category_id: int, category: CategoryUpdate):
    """
    Update an existing category.

    Args:
        db: Database session
        category_id: ID of category to update
        category: CategoryUpdate schema with new data

    Returns:
        Updated Category object or None if not found

    Process:
        1. Get existing category
        2. Update only provided fields
        3. Commit changes
        4. Return updated category
    """
    # Get existing category
    db_category = get_category(db, category_id)

    if db_category is None:
        return None

    # Update only the fields that were provided
    update_data = category.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_category, field, value)

    # Commit changes
    db.commit()
    db.refresh(db_category)

    return db_category


def delete_category(db: Session, category_id: int):
    """
    Delete a category.

    Args:
        db: Database session
        category_id: ID of category to delete

    Returns:
        Deleted Category object or None if not found

    Note:
        Due to cascade="all, delete-orphan" in the relationship,
        all transactions in this category will also be deleted.
    """
    db_category = get_category(db, category_id)

    if db_category is None:
        return None

    # Delete the category
    db.delete(db_category)
    db.commit()

    return db_category
