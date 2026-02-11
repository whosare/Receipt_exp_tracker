from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

#Our two models for our database
class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True) #inique id made for every user, related to user_id for expense
    email=Column(String, unique=True, index=True) #unique email for every user
    hashed_password=Column(String) #password for every login
    expenses=relationship("Expense ", back_populates="user")

class Expense(Base): 
    __tablename__="Expenses"
    id=Column(Integer, primary_key=True, index=True) #id for each expense
    user_id=Column(Integer, ForeignKey("users.id"))
    vendor=Column(String)
    expense_type=Column(String)
    amount=Column(Float)
    date=Column(String)
    user=relationship("User", back_populates="expenses")
