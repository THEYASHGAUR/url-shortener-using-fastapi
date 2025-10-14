from fastapi import FastAPI
from .database import Base, engine
from .routes import url_routes

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI URL Shortener")

# Include routes
app.include_router(url_routes.router)
