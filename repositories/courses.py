from database import close_db_connection, connect_to_db


async def get_courses():
    conn = await connect_to_db()
    try:
        query = """
        SELECT 
            c.id AS course_id,
            c.course,
            c.mentor,
            c.title,
            COUNT(DISTINCT uc.id_user) AS jumlah_peserta
        FROM 
            public.courses c
        LEFT JOIN 
            public.userCourse uc ON c.id = uc.id_course
        GROUP BY 
            c.id, c.course, c.mentor, c.title
        HAVING
            COUNT(DISTINCT uc.id_user) > 0;
        """
        courses = await conn.fetch(query)
        return [dict(course) for course in courses]
    finally:
        await close_db_connection(conn)
