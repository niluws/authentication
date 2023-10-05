from fastapi import FastAPI, HTTPException,status
from config import database
import schemas


app = FastAPI()


@app.post("/registration/", response_model=schemas.User)
def register(user: schemas.UserCreate):
    existing_user = database.collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail='Email already exists')

    result = database.collection.insert_one(dict(user))

    user_id = str(result.inserted_id)

    return schemas.User(id=user_id, full_name=user.full_name, email=user.email)
    

@app.post("/login/")
def login(user: schemas.UserLogin):
    user_data = database.collection.find_one({"email": user.email})

    if user_data is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email does not exist")

    if user_data["password"] != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
    
    return {"message": "Login successful"}