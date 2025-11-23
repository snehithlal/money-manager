"""
Schemas package - Pydantic schemas organized by entity.

This package contains Pydantic models for request/response validation.
Each file contains schemas for a different entity.
"""

from .category import (
    CategoryBase,
    CategoryCreate,
    CategoryUpdate,
    Category
)
from .transaction import (
    TransactionBase,
    TransactionCreate,
    TransactionUpdate,
    Transaction
)
from .analytics import (
    MonthlySummary,
    CategorySummary
)

__all__ = [
    # Category schemas
    "CategoryBase",
    "CategoryCreate",
    "CategoryUpdate",
    "Category",
    # Transaction schemas
    "TransactionBase",
    "TransactionCreate",
    "TransactionUpdate",
    "Transaction",
    # Analytics schemas
    "MonthlySummary",
    "CategorySummary",
]
