"""
API v1 Router Aggregation.

This module aggregates all v1 API endpoints into a single router.
All routes will be prefixed with /api/v1

Benefits:
- API versioning support (can add v2, v3 later)
- Clean separation of API versions
- Easy to deprecate old versions
- Industry standard pattern

Usage in main.py:
    from app.api.v1.router import api_v1_router
    app.include_router(api_v1_router)
"""

from fastapi import APIRouter
from app.routers import categories, transactions, analytics, auth

# Create the v1 API router
# All routes registered here will be prefixed with /api/v1
api_v1_router = APIRouter(prefix="/api/v1")

# Register authentication endpoints
# Final routes: /api/v1/auth/*
api_v1_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

# Register category endpoints
# Final routes: /api/v1/categories/*
api_v1_router.include_router(
    categories.router,
    prefix="/categories",
    tags=["Categories"]
)

# Register transaction endpoints
# Final routes: /api/v1/transactions/*
api_v1_router.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["Transactions"]
)

# Register analytics endpoints
# Final routes: /api/v1/analytics/*
api_v1_router.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["Analytics"]
)

# Future routers can be added here:
# api_v1_router.include_router(
#     budgets.router,
#     prefix="/budgets",
#     tags=["Budgets"]
# )
#
# api_v1_router.include_router(
#     users.router,
#     prefix="/users",
#     tags=["Users"],
#     dependencies=[Depends(get_current_user)]  # Add auth
# )
