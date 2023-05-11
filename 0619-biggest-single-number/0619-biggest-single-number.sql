# Write your MySQL query statement below
SELECT MAX(num) AS num FROM (SELECT COUNT(num) AS count_num, num FROM myNumbers GROUP BY num) AS SubQuery WHERE SubQuery.count_num = 1;