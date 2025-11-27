"""
FastAPI main application file.

This is the entry point for the FastAPI application.
It sets up:
- CORS (Cross-Origin Resource Sharing) to allow frontend to communicate with backend
- API versioning (v1)
- Database initialization
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .api.v1.router import api_v1_router

# Create all database tables
# This will create tables based on our models if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Money Manager API",
    description="Backend API for Money Manager application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
# This allows our Next.js frontend to make requests to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
    ],
    allow_origin_regex="https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API v1 router
# All v1 endpoints will be available at /api/v1/*
app.include_router(api_v1_router)

# Future API versions can be added here:
# from .api.v2.router import api_v2_router
# app.include_router(api_v2_router)


@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "message": "Money Manager API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs",
        "api_v1": "/api/v1"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "1.0.0"}
