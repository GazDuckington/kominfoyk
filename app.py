from fastapi import Body, FastAPI, HTTPException
from passlib.context import CryptContext
from database import connect_to_db, close_db_connection
from database.objects import User
from utils import dict_to_object

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/login/")
async def login(username: str = Body(...), password: str = Body(...)):
    conn = await connect_to_db()
    try:
        user = await conn.fetchrow("SELECT * FROM users WHERE username = $1", username)
        user_dict = dict(user) if user else None
        if user_dict is None:
            raise HTTPException(status_code=500, detail="Invalid credentials")

        user_obj = dict_to_object(user_dict, User)
        if user is None:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        return {"message": "Login successful", "user_id": user["id"]}
    finally:
        await close_db_connection(conn)


@app.post("/register/")
async def register(username: str, email: str, password: str):
    conn = await connect_to_db()
    try:
        hashed_password = pwd_context.hash(password)
        await conn.execute(
            "INSERT INTO users (username, email, password) VALUES ($1, $2, $3)",
            username,
            email,
            hashed_password,
        )
        return {"message": "User created"}
    finally:
        await close_db_connection(conn)
