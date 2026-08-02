# Write your MySQL query statement below
-- Combine data from two tables based on a matching column
SELECT 
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;

