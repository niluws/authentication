from pydantic import BaseModel
from pydantic import EmailStr

class UserBase(BaseModel):
    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    # class Config:
    #     orm_mode = True

class UserLogin(BaseModel):
    email:EmailStr
    password:str
