from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from model import User
from schemas import UserCreate, UserResponse
import bcrypt
from routes.auth import get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])

# --------------------------------------------
# Create User (Signup)
# --------------------------------------------
@router.post("/signup", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # Hash password
    hashed_pw = get_password_hash(user.password)

    new_user = User(
        username=user.username,
        phno=user.phno,
        password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user")
def get_user(db: Session = Depends(get_db)):
    
    users = db.query(User).all()
    return users


@router.delete("/users")
def del_users(db: Session = Depends(get_db)):
    deleted_count = db.query(User).delete()
    db.commit()
    return{"deleted users":deleted_count}

    