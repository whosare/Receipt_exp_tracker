from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
class UserLogin(BaseModel):
    email: str
    password: str
class ExpenseCreate(BaseModel):
    vendor: str
    expense_type: str
    amount: float
    date: str

