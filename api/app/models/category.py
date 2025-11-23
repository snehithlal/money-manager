"""
Category database model.

Defines the structure of the 'categories' table.
Categories are used to organize transactions (e.g., Food, Transport, Salary).
"""

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
import enum
from ..database import Base


class TransactionType(str, enum.Enum):
    """Enum for transaction types"""
    INCOME = "income"
    EXPENSE = "expense"


class Category(Base):
    """
    Category model for organizing transactions.

    Attributes:
        id: Primary key
        name: Category name (e.g., "Food", "Salary")
        type: Either "income" or "expense"
        color: Hex color code for UI display (e.g., "#FF5733")
        icon: Icon name or emoji for UI display

    Relationships:
        transactions: All transactions in this category
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    color = Column(String, default="#6366f1")  # Default indigo color
    icon = Column(String, default="💰")  # Default money emoji

    # Relationship: One category can have many transactions
    transactions = relationship("Transaction", back_populates="category", cascade="all, delete-orphan")
