"""
CRUD package - Database operations organized by entity.

This package contains functions for Create, Read, Update, Delete operations.
Each file contains CRUD operations for a different entity.
"""

from .category import (
    get_category,
    get_categories,
    get_categories_by_type,
    create_category,
    update_category,
    delete_category
)

from .transaction import (
    get_transaction,
    get_transactions,
    get_transactions_by_month,
    create_transaction,
    update_transaction,
    delete_transaction
)

from .analytics import (
    get_monthly_summary,
    get_category_summary
)

__all__ = [
    # Category CRUD
    "get_category",
    "get_categories",
    "get_categories_by_type",
    "create_category",
    "update_category",
    "delete_category",
    # Transaction CRUD
    "get_transaction",
    "get_transactions",
    "get_transactions_by_month",
    "create_transaction",
    "update_transaction",
    "delete_transaction",
    # Analytics CRUD
    "get_monthly_summary",
    "get_category_summary",
]
