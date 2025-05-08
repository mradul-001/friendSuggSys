from fastapi import APIRouter, Request
from app.db import get_db

router = APIRouter()

@router.post("/register")
async def register_user(request: Request):
    data = await request.json()
    name = data["name"]
    email = data["email"]
    password = data["password"]

    db = get_db()
    db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
               (name, email, password))
    db.commit()
    return {"status": "success", "message": "User registered"}

