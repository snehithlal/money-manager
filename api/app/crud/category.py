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
    """
    return db.query(Category).filter(Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100, user_id: int = None):
    """
    Get all categories with pagination, filtered by user.
    """
    return db.query(Category).filter(Category.user_id == user_id).offset(skip).limit(limit).all()


def get_categories_by_type(db: Session, type: str, user_id: int = None):
    """
    Get categories filtered by type (income/expense) and user.
    """
    return db.query(Category).filter(
        Category.type == type,
        Category.user_id == user_id
    ).all()


def create_category(db: Session, category: CategoryCreate, user_id: int):
    """
    Create a new category for a user.
    """
    db_category = Category(
        name=category.name,
        type=category.type,
        color=category.color,
        icon=category.icon,
        user_id=user_id
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category: CategoryUpdate, user_id: int):
    """
    Update an existing category.
    """
    db_category = db.query(Category).filter(Category.id == category_id, Category.user_id == user_id).first()
    if db_category:
        update_data = category.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int, user_id: int):
    """
    Delete a category.
    """
    db_category = db.query(Category).filter(Category.id == category_id, Category.user_id == user_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category
