
INSERT INTO public.users (username, email, "password") VALUES
('Andi', 'andi@andi.com', '12345'),
('Budi', 'budi@budi.com', '67890'),
('Caca', 'caca@caca.com', 'abcde'),
('Deni', 'deni@deni.com', 'fghij'),
('Euis', 'euis@euis.com', 'klmno'),
('Fafa', 'fafa@fafa.com', 'pqrst');

INSERT INTO public.courses (course, mentor, title) VALUES
('C++', 'Ari', 'Dr.'),
('C#', 'Ari', 'Dr.'),
('C#', 'Ari', 'Dr.'),
('CSS', 'Cania', 'S.Kom'),
('HTML', 'Cania', 'S.Kom'),
('Javascript', 'Cania', 'S.Kom'),
('Python', 'Barry', 'S.T.'),
('Micropython', 'Barry', 'S.T.'),
('Java', 'Darren', 'M.T.'),
('Ruby', 'Darren', 'M.T.');


INSERT INTO public.userCourse (id_user, id_course) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(2, 6),
(3, 7),
(3, 8),
(3, 9),
(4, 1),
(4, 3),
(4, 5),
(5, 2),
(5, 4),
(3, 6),
(6, 7),
(6, 8),
(6, 9);
