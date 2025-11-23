"""
Transaction database model.

Defines the structure of the 'transactions' table.
Transactions represent individual income or expense records.
"""

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import date
from .category import TransactionType
from ..database import Base


class Transaction(Base):
    """
    Transaction model for income and expense records.

    Attributes:
        id: Primary key
        amount: Transaction amount (positive number)
        description: Optional description of the transaction
        date: Date of the transaction
        category_id: Foreign key to Category
        type: Either "income" or "expense"

    Relationships:
        category: The category this transaction belongs to
    """
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False, default=date.today)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)

    # Relationship: Each transaction belongs to one category
    category = relationship("Category", back_populates="transactions")
