"""
Seed script to create admin user and sample data.

Run this script to populate the database with:
- Admin user
- Sample categories
- Sample transactions
"""

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import User, Category, Transaction
from app.core.security import get_password_hash
from datetime import date, timedelta


def create_admin_user(db: Session):
    """Create admin user if not exists."""
    admin_email = "admin@example.com"

    # Check if admin already exists
    existing_admin = db.query(User).filter(User.email == admin_email).first()
    if existing_admin:
        print(f"✓ Admin user already exists: {admin_email}")
        return existing_admin

    # Create admin user
    admin = User(
        email=admin_email,
        hashed_password=get_password_hash("admin123"),
        is_active=True
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    print(f"✓ Created admin user: {admin_email}")
    print(f"  Password: admin123")
    return admin


def create_sample_categories(db: Session, user_id: int):
    """Create sample categories for the user."""
    categories_data = [
        # Income categories
        {"name": "Salary", "type": "income", "color": "#10b981", "icon": "💰"},
        {"name": "Freelance", "type": "income", "color": "#3b82f6", "icon": "💼"},
        {"name": "Investment", "type": "income", "color": "#8b5cf6", "icon": "📈"},

        # Expense categories
        {"name": "Groceries", "type": "expense", "color": "#ef4444", "icon": "🛒"},
        {"name": "Rent", "type": "expense", "color": "#f59e0b", "icon": "🏠"},
        {"name": "Transportation", "type": "expense", "color": "#06b6d4", "icon": "🚗"},
        {"name": "Entertainment", "type": "expense", "color": "#ec4899", "icon": "🎬"},
        {"name": "Healthcare", "type": "expense", "color": "#14b8a6", "icon": "⚕️"},
        {"name": "Utilities", "type": "expense", "color": "#f97316", "icon": "💡"},
        {"name": "Food & Dining", "type": "expense", "color": "#84cc16", "icon": "🍔"},
    ]

    created_categories = []
    for cat_data in categories_data:
        # Check if category already exists
        existing = db.query(Category).filter(
            Category.name == cat_data["name"],
            Category.user_id == user_id
        ).first()

        if not existing:
            category = Category(**cat_data, user_id=user_id)
            db.add(category)
            created_categories.append(category)

    db.commit()
    print(f"✓ Created {len(created_categories)} sample categories")
    return db.query(Category).filter(Category.user_id == user_id).all()


def create_sample_transactions(db: Session, user_id: int, categories: list):
    """Create sample transactions for the user."""
    # Get category IDs by name
    cat_map = {cat.name: cat.id for cat in categories}

    today = date.today()
    transactions_data = [
        # Income transactions
        {"amount": 5000.00, "description": "Monthly salary", "date": today.replace(day=1), "category_id": cat_map.get("Salary"), "type": "income"},
        {"amount": 1500.00, "description": "Freelance project", "date": today - timedelta(days=5), "category_id": cat_map.get("Freelance"), "type": "income"},

        # Expense transactions
        {"amount": 1200.00, "description": "Monthly rent", "date": today.replace(day=1), "category_id": cat_map.get("Rent"), "type": "expense"},
        {"amount": 250.50, "description": "Weekly groceries", "date": today - timedelta(days=2), "category_id": cat_map.get("Groceries"), "type": "expense"},
        {"amount": 45.00, "description": "Gas station", "date": today - timedelta(days=3), "category_id": cat_map.get("Transportation"), "type": "expense"},
        {"amount": 89.99, "description": "Netflix & Spotify", "date": today - timedelta(days=7), "category_id": cat_map.get("Entertainment"), "type": "expense"},
        {"amount": 150.00, "description": "Electricity bill", "date": today - timedelta(days=10), "category_id": cat_map.get("Utilities"), "type": "expense"},
        {"amount": 65.00, "description": "Restaurant dinner", "date": today - timedelta(days=1), "category_id": cat_map.get("Food & Dining"), "type": "expense"},
        {"amount": 120.00, "description": "Groceries", "date": today - timedelta(days=9), "category_id": cat_map.get("Groceries"), "type": "expense"},
        {"amount": 30.00, "description": "Uber rides", "date": today - timedelta(days=4), "category_id": cat_map.get("Transportation"), "type": "expense"},
    ]

    created_count = 0
    for trans_data in transactions_data:
        if trans_data["category_id"]:  # Only create if category exists
            transaction = Transaction(**trans_data, user_id=user_id)
            db.add(transaction)
            created_count += 1

    db.commit()
    print(f"✓ Created {created_count} sample transactions")


def seed_database():
    """Main seed function."""
    print("\n🌱 Seeding database...\n")

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create database session
    db = SessionLocal()

    try:
        # Create admin user
        admin = create_admin_user(db)

        # Create sample categories
        categories = create_sample_categories(db, admin.id)

        # Create sample transactions
        create_sample_transactions(db, admin.id, categories)

        print("\n✅ Database seeded successfully!\n")
        print("=" * 50)
        print("Admin Credentials:")
        print("  Email: admin@example.com")
        print("  Password: admin123")
        print("=" * 50)
        print("\nTest User Credentials:")
        print("  Email: test@example.com")
        print("  Password: password123")
        print("=" * 50)

    except Exception as e:
        print(f"\n❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
