from sqlalchemy import Column , Integer , String , Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String, unique=True , nullable= False)
    phno = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    expenses = relationship("Expenses", back_populates="owner")
    
class Expenses(Base):
    
    __tablename__ = "expenses"
    
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String, ForeignKey("users.username"), nullable= False)
    day= Column(Integer,nullable=False)
    month= Column(Integer,nullable=False)
    year= Column(Integer,nullable=False)
    datetime = Column(String,nullable=False)
    item_name = Column(String,nullable=False)
    cost = Column(Float, nullable=False)
    
    owner = relationship("User", back_populates="expenses")
    