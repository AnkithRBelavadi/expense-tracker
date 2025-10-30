from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from model import Expenses , User
from schemas import ExpenseResponse ,ExpenseBase
from datetime import datetime
router = APIRouter(prefix="/expenses")
from routes.auth import get_current_user
from sqlalchemy import func

@router.post("/create")
async def create_expense(expense : ExpenseBase ,db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    
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
async def lisitng_expenses(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expenses = db.query(Expenses).filter(Expenses.username == current_user.username).all()
    return expenses

@router.get("/list_all")
async def lisitng_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expenses).all()
    return expenses

@router.delete("/list")
async def del_expenses(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    expenses_count = db.query(Expenses).filter(Expenses.username==current_user.username).delete()
    db.commit()
    return {"Deleted entires":expenses_count}
    
@router.get("/daily_sum")
async def get_daily(day: int = int(datetime.now().day), db: Session=Depends(get_db), current_user = Depends(get_current_user)):
    
    month = datetime.now().month
    year= datetime.now().year
    
    expenses = db.query(func.sum(Expenses.cost)).filter(Expenses.username==current_user.username).filter(Expenses.year==year).filter(Expenses.month==month).filter(Expenses.day==day).scalar()
    items = db.query(Expenses).filter(
        Expenses.username==current_user.username,
        Expenses.year == year,
        Expenses.month == month,
        Expenses.day == day
    ).all()
    op_dict = {
        "Item details":[],
        "Total":0
    }
    for item in items:
        op_dict["Item details"].append([item.item_name , item.cost , item.datetime])
        
    op_dict["Total"]=expenses
    
    return op_dict

@router.get("/monthly_sum")
async def get_daily(month: int , year : int ,db: Session=Depends(get_db), current_user = Depends(get_current_user)):
    
    
    expenses = db.query(func.sum(Expenses.cost)).filter(Expenses.username==current_user.username).filter(Expenses.year==year).filter(Expenses.month==month).scalar()
    items = db.query(Expenses).filter(
        Expenses.username==current_user.username,
        Expenses.year == year,
        Expenses.month == month
    ).all()
    op_dict = {
        "Item details":[],
        "Total":0
    }
    for item in items:
        op_dict["Item details"].append([item.item_name , item.cost , item.datetime])
        
    op_dict["Total"]=expenses
    
    return op_dict

@router.get("/yearly_sum")
async def get_daily( year : int ,db: Session=Depends(get_db), current_user = Depends(get_current_user)):
    
    
    expenses = db.query(func.sum(Expenses.cost)).filter(Expenses.username==current_user.username).filter(Expenses.year==year).scalar()
    items = db.query(Expenses).filter(
        Expenses.username==current_user.username,
        Expenses.year == year
    ).all()
    op_dict = {
        "Item details":[],
        "Total":0
    }
    for item in items:
        op_dict["Item details"].append([item.item_name , item.cost , item.datetime])
        
    op_dict["Total"]=expenses
    
    return op_dict