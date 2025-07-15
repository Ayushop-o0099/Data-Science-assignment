

CREATE DATABASE college_db;
USE college_db;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);

INSERT INTO students (name, age, department) VALUES
('Alice', 21, 'Computer Science'),
('Bob', 19, 'Mechanical'),
('John', 22, 'Electrical'),
('David', 23, 'Computer Science'),
('Angela', 20, 'Civil');

SELECT * FROM students;
SELECT * FROM students WHERE age > 20;
UPDATE students SET department = 'Electronics' WHERE name = 'John';
DELETE FROM students WHERE id = 3;
SELECT * FROM students ORDER BY age DESC;
SELECT DISTINCT department FROM students;
SELECT COUNT(*) AS total_students FROM students;
RENAME TABLE students TO student_info;
ALTER TABLE student_info ADD COLUMN email VARCHAR(100);
SELECT * FROM student_info WHERE name LIKE 'A%';
SELECT * FROM student_info WHERE age BETWEEN 18 AND 25;
SELECT * FROM student_info ORDER BY age DESC LIMIT 1;
SELECT * FROM student_info LIMIT 3;

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

INSERT INTO courses VALUES
(101, 'Database Systems', 4),
(102, 'Operating Systems', 3),
(103, 'Data Structures', 3);

SELECT * FROM student_info WHERE department = 'Computer Science';
SELECT * FROM student_info WHERE department IN ('Civil', 'Mechanical');
SELECT * FROM student_info WHERE age BETWEEN 20 AND 30;
SELECT NOW();
SELECT name AS student_name FROM student_info;
SELECT * FROM student_info WHERE department != 'Mechanical';
DELETE FROM student_info;



CREATE TABLE marks (
    student_id INT,
    subject VARCHAR(50),
    marks INT
);

INSERT INTO marks VALUES
(1, 'Math', 85),
(2, 'Math', 75),
(1, 'Science', 90),
(2, 'Science', 88),
(4, 'Math', 95);

SELECT si.name, m.subject, m.marks
FROM student_info si
JOIN marks m ON si.id = m.student_id;

SELECT student_id, AVG(marks) AS avg_marks
FROM marks
GROUP BY student_id;

SELECT student_id, SUM(marks) AS total_marks
FROM marks
GROUP BY student_id;

SELECT student_id, SUM(marks) AS total
FROM marks
GROUP BY student_id
HAVING total > 200;

SELECT age, COUNT(*) AS count
FROM student_info
GROUP BY age
HAVING count > 1;

SELECT * FROM student_info si
INNER JOIN marks m ON si.id = m.student_id;

SELECT * FROM student_info si
LEFT JOIN marks m ON si.id = m.student_id;

SELECT * FROM student_info si
RIGHT JOIN marks m ON si.id = m.student_id;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100)
);

CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES student_info(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

SELECT * FROM marks
WHERE marks = (SELECT MAX(marks) FROM marks);

CREATE VIEW student_totals AS
SELECT si.name, SUM(m.marks) AS total_marks
FROM student_info si
JOIN marks m ON si.id = m.student_id
GROUP BY si.name;

SELECT * FROM marks
WHERE marks > (SELECT AVG(marks) FROM marks);

DELIMITER //
CREATE PROCEDURE AddStudent(
    IN s_name VARCHAR(50), IN s_age INT, IN s_dept VARCHAR(50)
)
BEGIN
    INSERT INTO student_info (name, age, department) VALUES (s_name, s_age, s_dept);
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateDepartment(
    IN s_id INT, IN new_dept VARCHAR(50)
)
BEGIN
    UPDATE student_info SET department = new_dept WHERE id = s_id;
END;
//
DELIMITER ;

DELIMITER //
CREATE FUNCTION GetGrade(m INT) RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    DECLARE g VARCHAR(10);
    IF m >= 90 THEN SET g = 'A';
    ELSEIF m >= 75 THEN SET g = 'B';
    ELSEIF m >= 60 THEN SET g = 'C';
    ELSE SET g = 'D';
    END IF;
    RETURN g;
END;
//
DELIMITER ;

CREATE TABLE student_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    action_time DATETIME
);

DELIMITER //
CREATE TRIGGER log_insert
AFTER INSERT ON student_info
FOR EACH ROW
BEGIN
    INSERT INTO student_log (name, action_time)
    VALUES (NEW.name, NOW());
END;
//
DELIMITER ;

START TRANSACTION;
UPDATE student_info SET age = age + 1 WHERE id = 1;
UPDATE student_info SET age = age + 1 WHERE id = 2;
COMMIT;

SELECT name, COUNT(*) AS count
FROM student_info
GROUP BY name
HAVING count > 1;



CREATE INDEX idx_name ON student_info(name);

SELECT MAX(marks) AS second_highest
FROM marks
WHERE marks < (SELECT MAX(marks) FROM marks);

DROP TABLE courses;
