"""
Vercel serverless function entry point.
"""
import sys
import os

# Add the backend directory to the path
# This allows us to import 'app' from 'backend/app'
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(os.path.dirname(current_dir), 'backend')
sys.path.insert(0, backend_dir)

# Import FastAPI app
from app.main import app

# Export for Vercel
# Don't rename - Vercel looks for 'app'
