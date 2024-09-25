import asyncpg

DATABASE_URL = "postgresql://admin:adminpass@localhost:5432/db_kominfo"


async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)


async def close_db_connection(conn):
    await conn.close()
