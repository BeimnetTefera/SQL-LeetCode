# Write your MySQL query statement below
SELECT
    product_name,
    SUM(ord.unit) AS unit
FROM Products AS pr
LEFT JOIN Orders AS ord
    ON pr.product_id = ord.product_id
    AND MONTH(order_date) = 2
GROUP BY pr.product_name, YEAR(ord.order_date)
HAVING SUM(ord.unit) >= 100 