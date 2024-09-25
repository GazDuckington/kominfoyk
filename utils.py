from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import datetime

from database.objects import User
from repositories.users import get_user_by_id

SECRET_KEY = "your_secret_key"  # Replace with a strong secret key
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def dict_to_object(data: dict, cls):
    filtered_data = {
        key: value
        for key, value in data.items()
        if key in cls.__init__.__code__.co_varnames
    }
    return cls(**filtered_data)


def create_jwt(user_id: int, level: str):
    expiration = datetime.datetime.now() + datetime.timedelta(hours=1)
    payload = {
        "sub": user_id,
        "level": level,
        "exp": expiration,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


async def verify_user_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = payload.get("sub")
        user_rep = await get_user_by_id(user)
        print(f"INI: {user_rep}")
        if user is None or user_rep is None:
            raise credentials_exception
        return dict_to_object(user_rep, User)
    except jwt.PyJWTError as e:
        raise credentials_exception from e
