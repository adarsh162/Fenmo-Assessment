from app.core.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
from app.models.expense import Expense
from app.api.v1 import router as api_router

# Create tables on startup (Only if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION, redirect_slashes=False)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router.router, prefix="/api/v1")

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy", "version": settings.VERSION}
