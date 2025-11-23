"""
Vercel serverless function entry point.

This file is required for deploying FastAPI to Vercel.
It exports the FastAPI app so Vercel can run it as a serverless function.
"""

from app.main import app

# Vercel looks for a variable named 'app' or 'handler'
# We're exporting our FastAPI app instance
handler = app
