-------------------------------------Create Database

CREATE DATABASE school_management;
USE school_management;

------------------------------------Create Table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    class_id INT
);

CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject_id INT
);
CREATE TABLE classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50)
);

CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(50)
);

CREATE TABLE student_subjects (
    student_id INT,
    subject_id INT,
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

CREATE TABLE teacher_subjects (
    teacher_id INT,
    subject_id INT,
    PRIMARY KEY (teacher_id, subject_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

--------------------------------------------------Data Insert

INSERT INTO students (first_name, last_name, age, class_id) VALUES
('John', 'Doe', 14, 1),
('Emma', 'Stone', 13, 2),
('Liam', 'Brown', 15, 3),
('Olivia', 'Johnson', 14, 1),
('Sophia', 'Wilson', 13, 2);

INSERT INTO teachers (first_name, last_name, subject_id) VALUES
('Michael', 'Smith', 1),
('Emily', 'Davis', 2),
('Daniel', 'Garcia', 3),
('Linda', 'Martinez', 4);

INSERT INTO classes (class_name) VALUES
('Grade 1'),
('Grade 2'),
('Grade 3');

INSERT INTO subjects (subject_name) VALUES
('Mathematics'),
('Science'),
('English'),
('History');

INSERT INTO student_subjects (student_id, subject_id) VALUES
(1, 1), (1, 2),
(2, 2), (2, 3),
(3, 1), (3, 3), (3, 4),
(4, 1), (4, 4),
(5, 2), (5, 3);

INSERT INTO teacher_subjects (teacher_id, subject_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(1, 2),
(2, 3);

------------------------------------------------Sql Queries

SELECT first_name, last_name FROM students;

SELECT first_name, last_name, age FROM students WHERE age = 14;

SELECT class_name FROM classes;

SELECT first_name, last_name FROM teachers;

SELECT subject_name FROM subjects;

SELECT s.first_name, s.last_name, c.class_name 
FROM students s
JOIN classes c ON s.class_id = c.class_id;

SELECT sub.subject_name 
FROM student_subjects ss
JOIN subjects sub ON ss.subject_id = sub.subject_id
WHERE ss.student_id = 1;

SELECT t.first_name, t.last_name 
FROM teachers t
JOIN teacher_subjects ts ON t.teacher_id = ts.teacher_id
JOIN subjects sub ON ts.subject_id = sub.subject_id
WHERE sub.subject_name = 'Mathematics';

SELECT c.class_name, COUNT(s.student_id) AS total_students
FROM classes c
LEFT JOIN students s ON c.class_id = s.class_id
GROUP BY c.class_name;

SELECT s.first_name, s.last_name 
FROM students s
JOIN student_subjects ss ON s.student_id = ss.student_id
JOIN subjects sub ON ss.subject_id = sub.subject_id
WHERE sub.subject_name = 'Science';
