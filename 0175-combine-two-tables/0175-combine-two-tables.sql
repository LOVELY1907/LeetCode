# Write your MySQL query statement below
-- Combine data from two tables based on a matching column
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON a.personId = p.personId;  -- Matching condition
