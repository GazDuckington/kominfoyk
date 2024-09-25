-- 4
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
    public.courses c ON uc.id_course = c.id;

-- 5
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
WHERE
	c.title LIKE 'S%';

-- 6
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
WHERE
	c.title NOT LIKE 'S%';

-- 7
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

-- 8
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

-- 9
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
