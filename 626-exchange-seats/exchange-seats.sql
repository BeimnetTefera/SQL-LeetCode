# Write your MySQL query statement below

SELECT
    id,
    COALESCE(
    CASE
        WHEN id % 2 != 0 THEN next_student
        WHEN id % 2 = 0 THEN prev_student
    END, student) AS student
FROM(
SELECT
    id,
    LEAD(student) OVER (ORDER BY id) AS next_student,
    LAG(student) OVER(ORDER BY id) AS prev_student,
    student
FROM Seat) AS temp;