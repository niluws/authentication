from fastapi import FastAPI, HTTPException, Depends,responses,status
from sqlalchemy.orm import Session
from config import database
import models,schemas


models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()

@app.post("/registration/",response_model=schemas.User)
def register(user: schemas.UserCreate,db: Session = Depends(get_db)):
  
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail='Email already exists')
    
    user = models.User(full_name=user.full_name,email=user.email,password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
    

@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user.email).first()

    if user is None or user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")


    return {"message": "Login successful"}