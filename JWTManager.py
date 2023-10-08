import jwt
from datetime import datetime, timedelta



class AuthHandler:
    SECRET_KEY = "e850730693d632d699dedab3ced649a8badad345dae49c20ab9989622b840868"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 10
    REFRESH_TOKEN_EXPIRE_MINUTES = 1440

    
    def create_access_token(cls, data: dict):
        expire = datetime.utcnow() + timedelta(seconds=cls.ACCESS_TOKEN_EXPIRE_MINUTES)
        data.update({"exp": expire})
        return jwt.encode(data, cls.SECRET_KEY, algorithm=cls.ALGORITHM)

    
    def create_refresh_token(cls, data: dict):
        expire = datetime.utcnow() + timedelta(minutes=cls.REFRESH_TOKEN_EXPIRE_MINUTES)
        data.update({"exp": expire})
        return jwt.encode(data, cls.SECRET_KEY, algorithm=cls.ALGORITHM)

    
    def decode_token(cls, token: str):
        try:
            payload = jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"} 
        except jwt.DecodeError:
            return {'error':"Token is invalid"} 
