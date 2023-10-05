from sqlalchemy import create_engine
from pymongo import MongoClient
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# client = MongoClient("mongodb://localhost:27017/")
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# db=client.auth_db

# try:
#     client.admin.command('ping')
#     print('you successfully connected to mongodb')
# except Exception as e:
#     print(e)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
