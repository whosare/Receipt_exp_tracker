from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
import os
import secrets


SECRET_KEY=os.getenv("SECRET_KEY") #our secret authentication key is specified in .env file
ALGORITHM="HS256" #algorithm HMAC-SHA256, used for JWTs
ACCESS_TOKEN_EXPIRE=30 #how long the access token will be valid for 
pwd_contxt=CryptContext(schemes=["bcrypt"], deprecated="auto") #passlibs crypt context object

def hash_password(password : str): #password to be fetched
    return pwd_contxt.hash(password)

def verify_password(plain : str, hashed : str): #comparison of password from database and what is given
    return pwd_contxt.verify(plain, hashed) 

def create_access_token(data : dict):
    for_encode=data.copy() #copy of data
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE) #current time is added with 30 mins to create expire deadline
    for_encode.update({"exp":expire})
    return jwt.encode(for_encode, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme= OAuth2PasswordBearer(tokenUrl="login")

def get_current_user_email(token : str=Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")