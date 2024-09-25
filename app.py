from fastapi import FastAPI, Form, HTTPException, Depends, Request
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from fastapi.responses import HTMLResponse
from database import connect_to_db, close_db_connection
from database.objects import User
from repositories.courses import get_courses, get_course_fee, get_courses_by_med
from repositories.users import delete_user_by_id, get_user_by_id
from utils import create_jwt, dict_to_object, verify_user_token

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templates = Jinja2Templates(directory="templates")  # Directory for HTML templates


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return open("index.html").read()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    conn = await connect_to_db()
    try:
        # WARN: bad practice, should be hashed password
        user = await conn.fetchrow(
            "SELECT * FROM users WHERE username = $1 AND password = $2",
            username,
            password,
        )
        user_dict = dict(user) if user else None
        if user_dict is None:
            raise HTTPException(status_code=500, detail="Invalid credentials")

        user_obj = dict_to_object(user_dict, User)
        token = create_jwt(user_obj.id, user_obj.level)
        current_user = await verify_user_token(token)
        if user is None:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        return {
            "status": "true",
            "message": "Login successful",
            "user_id": user_obj.id,
            "level": user_obj.level,
            "access_token": token,
        }
    finally:
        await close_db_connection(conn)


@app.post("/register/")
async def register(
    username: str = Form(...), email: str = Form(...), password: str = Form(...)
):
    conn = await connect_to_db()
    try:
        existing_user = await conn.fetchrow(
            "SELECT * FROM users WHERE username = $1 OR email = $2", username, email
        )

        if existing_user:
            return {"status": "false", "message": "Username or email already exists."}
        # hashed_password = pwd_context.hash(password)
        await conn.execute(
            "INSERT INTO users (username, email, password) VALUES ($1, $2, $3)",
            username,
            email,
            password,
        )
        return {"status": "true", "message": "User created"}
    finally:
        await close_db_connection(conn)


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, current_user: User = Depends(verify_user_token)):
    if current_user.level != "admin":  # Check if user is admin
        raise HTTPException(status_code=403, detail="Operation not permitted")

    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    await delete_user_by_id(user_id)  # Call the delete function
    return {"status": "true", "message": "User deleted successfully"}


# courses:


@app.get("/courses", response_class=HTMLResponse)
async def read_courses(request: Request):
    courses = await get_courses()
    return templates.TemplateResponse(
        "courses.html", {"request": request, "courses": courses}
    )


@app.get("/courses/fee", response_class=HTMLResponse)
async def read_courses_fees(request: Request):
    courses = await get_course_fee()
    return templates.TemplateResponse(
        "courses-fee.html", {"request": request, "courses": courses}
    )


@app.get("/courses/sarjana", response_class=HTMLResponse)
async def read_courses_med(request: Request):
    courses = await get_courses_by_med(sarjana=True)
    return templates.TemplateResponse(
        "courses-med.html", {"request": request, "courses": courses}
    )


@app.get("/courses/nsarjana", response_class=HTMLResponse)
async def read_courses_med_ns(request: Request):
    courses = await get_courses_by_med(sarjana=False)
    return templates.TemplateResponse(
        "courses-med.html", {"request": request, "courses": courses}
    )
