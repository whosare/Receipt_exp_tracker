from sqlalchemy.orm import Session
import models, schemas
from authorization import hash_password

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw=hash_password(user.password)
    db_user=models.User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db : Session, email : str):
    return db.query(models.User).filter(models.User.email==email).first()

def create_expense(db: Session, user_id: int, expense_data: schemas.ExpenseCreate):
    expense = models.Expense(
        user_id=user_id,
        vendor=expense_data.vendor,
        expense_type=expense_data.expense_type,
        amount=expense_data.amount,
        date=expense_data.date
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_expenses_for_user(db : Session, user_id : int):
    return db.query(models.Expense).filter(models.Expense.user_id==user_id).all()