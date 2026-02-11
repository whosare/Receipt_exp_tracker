from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session 
from fastapi.security import OAuth2PasswordRequestForm
from database import SessionLocal, engine
import models, schemas, crud, authorization, ocr_util
import shutil
import os

models.Base.metadata.create_all(bind=engine) #creates our tables from database

router = APIRouter() #router creation

def get_db(): #db session obtaining
    db=SessionLocal() 
    try:
        yield db
    finally:
        db.close()


@router.post("/register") #register route
def register(user: schemas.UserCreate, db: Session=Depends(get_db)):
    existing_user=crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud.create_user(db, user)

@router.post("/login") #login route
def login(form_data: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user=crud.get_user_by_email(db, form_data.username)
    if not user or not authorization.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = authorization.create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post('/upload-receipt')
def upload_receipt(
    file: UploadFile=File(...),
    db: Session=Depends(get_db),
    token: str=Depends(authorization.oauth2_scheme)
):
    user_email = authorization.get_current_user_email(token)
    user = crud.get_user_by_email(db, user_email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Save uploaded file temporarily
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR processing
    text = ocr_util.extract_text(file_path)
    parsed_data = ocr_util.parse_receipt(text)
    os.remove(file_path)

    # Add expense to database
    expense_data = schemas.ExpenseCreate(
        vendor=parsed_data["vendor"],
        expense_type="Uncategorized",  # Default for now
        amount=parsed_data["amount"],
        date=parsed_data["date"]
    )
    return crud.create_expense(db, user.id, expense_data)

@router.get("/expenses")
def get_user_expenses(
    db: Session = Depends(get_db),
    token: str = Depends(authorization.oauth2_scheme)
):
    user_email = authorization.get_current_user_email(token)
    user = crud.get_user_by_email(db, user_email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return crud.get_expenses_for_user(db, user.id)