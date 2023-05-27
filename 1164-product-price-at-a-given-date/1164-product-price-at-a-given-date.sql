# Write your MySQL query statement below
SELECT DISTINCT products.product_id, IFNULL(temp.new_price,10) as price
FROM (SELECT product_id,new_price,rank() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rnk FROM Products WHERE change_date <= '2019-08-16')temp
RIGHT JOIN Products ON temp.product_id = products.product_id
WHERE temp.rnk = 1 OR temp.rnk IS NULL;