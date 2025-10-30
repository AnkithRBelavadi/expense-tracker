from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username : str
    phno : str

class UserCreate(UserBase):
    password : str

class UserLogin(BaseModel):
    username: str
    password:str
    
class UserResponse(UserBase):
    id: int

    class Config:
        #Enables SQL Alchemy model
        from_attributes = True 




class ExpenseBase(BaseModel):
    item_name: str
    cost: float
  # can keep as string or ISO timestamp


# class ExpenseCreate(ExpenseBase):
#     username: str


class ExpenseUpdate(BaseModel):
    item_name: Optional[str] = None
    cost: Optional[float] = None
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    datetime: Optional[str] = None


class ExpenseResponse(ExpenseBase):
    id: int
    username: str

    class Config:
        from_attributes = True
        
    
