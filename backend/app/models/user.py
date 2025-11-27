"""
User database model.

Defines the structure of the 'users' table.
"""

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    """
    User model for authentication and data ownership.

    Attributes:
        id: Primary key
        email: Unique email address
        hashed_password: Hashed password string
        is_active: Boolean flag for active status

    Relationships:
        categories: Categories created by this user
        transactions: Transactions created by this user
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationships
    categories = relationship("Category", back_populates="owner")
    transactions = relationship("Transaction", back_populates="owner")
