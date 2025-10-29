# Create database URL
# # Create Engine -> connect sqlalchemy  to db
# create SessionLocal -> each request gets a new db session
# Base -> all ORM will inherit from this
# get_db() ->

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./expenses.db"


#Required for sql alchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

#Create session
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
