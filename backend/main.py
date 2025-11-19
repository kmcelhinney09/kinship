from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import users, calendar, meals, chores

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kinship API", description="API for Family Command Center", version="0.1.0")

# CORS configuration
origins = [
    "http://localhost:5173",  # Vite dev server
    "http://localhost:4173",  # Vite preview
    "http://127.0.0.1:5173",
    "*" # Allow all for local dev convenience on Pi
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "app": "Kinship"}

# Include routers (commented out until created)
app.include_router(users.router)
app.include_router(calendar.router)
app.include_router(meals.router)
app.include_router(chores.router)
