from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from model import Expenses , User
from schemas import ExpenseResponse ,ExpenseBase
from datetime import datetime
router = APIRouter(prefix="/expenses")
from routes.auth import get_current_user

@router.post("/create")
def create_expense(expense : ExpenseBase ,db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    
    new_expense = Expenses(
    username=current_user.username,
    item_name= expense.item_name,
    cost= expense.cost,
    day= int(datetime.now().day),
    month= int(datetime.now().month),
    year= int(datetime.now().year),
    datetime= str(datetime.now())
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/list")
def lisitng_expenses(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expenses = db.query(Expenses).filter(Expenses.username == current_user.username).all()
    return expenses

@router.delete("/list")
def del_expenses(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expenses_count = db.query(Expenses).filter(Expenses.username==current_user.username).delete()
    db.commit()
    return {"Deleted entires":expenses_count}
    