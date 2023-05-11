# Write your MySQL query statement below
SELECT 
    employee_id,
    IFNULL(MAX(CASE WHEN primary_flag="Y" THEN department_id END),department_id) as department_id
    
FROM Employee
GROUP BY employee_id;