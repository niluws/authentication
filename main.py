from fastapi import FastAPI, HTTPException,status,Depends,Header
from config import database
import schemas,JWTManager

app = FastAPI()

db=database.DatabaseSingleton()
jwt_manager = JWTManager.AuthHandler()

@app.post("/register/")
def register(user: schemas.UserCreate):
    existing_user = db.collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail='Email already exists')

    result = db.collection.insert_one(dict(user))

    user_id = str(result.inserted_id)

    return {"user": schemas.User(id=user_id, full_name=user.full_name, email=user.email)}
    

@app.post("/login/")
def login(user: schemas.UserLogin):
    user_data = db.collection.find_one({"email": user.email})

    if user_data is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email does not exist")

    if user_data["password"] != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
    
    access_token = jwt_manager.create_access_token({"email": user.email})
    refresh_token = jwt_manager.create_refresh_token({"email": user.email})

    return {"message": "Login successful", "access_token": access_token, "refresh_token": refresh_token}




@app.get("/me/")
def me(authorization: str = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = authorization.split("Bearer ")[1]
    user = jwt_manager.decode_token(token)

    return { 'message': user }
