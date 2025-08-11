SELECT Name from artist
LIMIT 5;

SELECT * FROM album
LIMIT 5;

SELECT customer_id, SUM(total) AS total_spent
FROM invoice
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;