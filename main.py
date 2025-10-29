from fastapi import FastAPI
from database import engine
from model import Base
from routes import test_users , expenses , auth

# Create tables if not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker")

# Include routes
app.include_router(test_users.router)
app.include_router(expenses.router)
app.include_router(auth.router)
