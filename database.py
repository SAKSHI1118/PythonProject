from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql  

DATABASE_URL = "mysql+pymysql://fastapi_user:password@localhost:3306/product_db"

engine = create_engine(
    DATABASE_URL,
    pool_size=10,         
    max_overflow=20,    
    pool_recycle=3600,    
    echo=True         
)

SessionLocal = sessionmaker(
    autocommit=False,    
    autoflush=False,     
    bind=engine         
)

Base = declarative_base() 

