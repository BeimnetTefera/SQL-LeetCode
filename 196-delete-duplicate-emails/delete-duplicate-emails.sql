# Write your MySQL query statement below
DELETE FROM Person
WHERE id NOT IN (
    SELECT 
        id 
    FROM (
        SELECT
            id,
            ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rnk
        FROM Person
    ) t
    WHERE rnk = 1
);