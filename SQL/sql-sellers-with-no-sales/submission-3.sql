-- Write your query below
SELECT seller_name
FROM seller AS s
LEFT JOIN orders AS o ON s.seller_id = o.seller_id
AND o.sale_date >= '2020-01-01' AND o.sale_date <= '2020-12-31'
WHERE o.seller_id IS NULL
ORDER BY seller_name ASC;