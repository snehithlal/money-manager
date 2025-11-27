"""
Vercel serverless function entry point.
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import FastAPI app
from app.main import app

# Export for Vercel (newer runtime supports ASGI directly)
# Don't rename - Vercel looks for 'app'
