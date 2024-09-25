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


async def get_course_fee():
    conn = await connect_to_db()
    try:
        query = """
        SELECT 
            c.mentor,
            COUNT(DISTINCT uc.id_user) AS jumlah_peserta,
            COUNT(DISTINCT uc.id_user) * 2000000 AS total_fee
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


async def get_courses_by_med(sarjana: bool = True):
    conn = await connect_to_db()
    try:
        query = """
SELECT 
    uc.id_user, 
    u.username, 
    c.course, 
    c.mentor, 
    c.title 
FROM 
    public.userCourse uc
JOIN 
    public.users u ON uc.id_user = u.id
JOIN 
    public.courses c ON uc.id_course = c.id
        """
        if sarjana:
            query += " WHERE c.title LIKE 'S%';"
        else:
            query += " WHERE c.title NOT LIKE 'S%';"
        courses = await conn.fetch(query)
        return [dict(course) for course in courses]
    finally:
        await close_db_connection(conn)
