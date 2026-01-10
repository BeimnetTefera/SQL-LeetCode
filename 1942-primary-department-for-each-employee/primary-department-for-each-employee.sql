# Write your MySQL query statement below
SELECT 
    employee_id,
    department_id
FROM (
        SELECT 
            employee_id,
            department_id,
            ROW_NUMBER() OVER (
                PARTITION BY employee_id 
                ORDER BY primary_flag ASC
            ) AS rnk
        FROM Employee
) AS t
WHERE rnk = 1;