from fastapi import APIRouter
from app.db import get_db_connection

router = APIRouter(prefix="/users")

@router.get("/")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT NOW() AS time")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result
