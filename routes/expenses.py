from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from model import Expenses , User
from schemas import ExpenseCreate,ExpenseResponse
from datetime import datetime
router = APIRouter(prefix="/expenses")
from routes.auth import get_current_user

@router.post("/create")
def create_expense(expense : ExpenseCreate,db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    
    new_expense = Expenses(
    username=current_user.username,
    item_name= expense.item_name,
    cost= expense.cost,
    day= expense.day,
    month= expense.month,
    year= expense.year,
    datetime= expense.datetime 
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/list")
def lisitng_expenses(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expenses = db.query(Expenses).filter(Expenses.username == current_user.username).all()
    return expenses
    