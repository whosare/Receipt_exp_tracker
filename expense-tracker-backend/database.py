from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv() #load our environment variables

DATABASE_URL=os.getenv("DATABASE_URL") #fetch our database url
print("Loaded DATABASE_URL:", os.getenv("DATABASE_URL"))
 
engine=create_engine(DATABASE_URL) #connecting to postgresql

SessionLocal=sessionmaker(bind=engine, autoflush=False) #binds to our previous engine and requires commits
Base=declarative_base()

