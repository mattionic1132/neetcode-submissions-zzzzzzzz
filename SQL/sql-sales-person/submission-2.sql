-- Write your query below
SELECT sp.name 
FROM sales_person AS sp
WHERE sp.sales_id NOT IN(
    SELECT o.sales_id 
    FROM orders AS o
    LEFT JOIN company AS c ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
);