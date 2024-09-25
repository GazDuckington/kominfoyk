CREATE TABLE public.users (
	id serial PRIMARY KEY,
	username varchar NOT NULL,
	email varchar NOT NULL,
	"password" varchar NOT NULL,
	created_at timestamp DEFAULT CURRENT_TIMESTAMP NULL,
	updated_at timestamp DEFAULT CURRENT_TIMESTAMP NULL
);

CREATE TABLE public.courses (
	id serial PRIMARY KEY,
	course varchar NOT NULL,
	mentor varchar NOT NULL,
	title varchar NOT NULL
);

CREATE TABLE public.userCourse (
	id serial PRIMARY KEY,
    id_user INT NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    id_course INT NOT NULL REFERENCES public.courses(id) ON DELETE CASCADE
);
