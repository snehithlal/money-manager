"""
Database configuration and connection setup.

This module handles:
- Database connection using SQLAlchemy
- Support for both SQLite (local development) and PostgreSQL (production)
- Session management for database operations
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment variable, default to SQLite for local development
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./money_manager.db")

# For SQLite, we need to enable check_same_thread=False to allow multiple threads
# For PostgreSQL, this is not needed
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    # For PostgreSQL (Vercel deployment)
    engine = create_engine(DATABASE_URL)

# SessionLocal is a factory for creating database sessions
# Each request will get its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all our database models
Base = declarative_base()

# Dependency function to get database session
# This will be used in our API endpoints
def get_db():
    """
    Generator function that yields a database session.
    Ensures the session is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Import models to register them with Base
# This must be done after Base is created
from .models import Category, Transaction  # noqa: E402
