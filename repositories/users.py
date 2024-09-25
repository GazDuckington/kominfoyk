from database import close_db_connection, connect_to_db


async def get_user_by_id(user_id: int):
    conn = await connect_to_db()
    try:
        user = await conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)
        return dict(user) if user else None
    finally:
        await close_db_connection(conn)


async def delete_user_by_id(user_id: int):
    conn = await connect_to_db()
    try:
        return await conn.execute("DELETE FROM users WHERE id = $1", user_id)
    finally:
        await close_db_connection(conn)
