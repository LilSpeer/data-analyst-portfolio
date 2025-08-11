-- 1. Customer Segment Analysis based on Purchase Behavior

    -- Find the top 10 customers by total spent
SELECT  invoice.customer_id, 
        customer.first_name || ' ' || customer.last_name AS CustomerName, 
        customer.country,
        SUM(invoice.total) AS TotalSpent
FROM invoice
JOIN customer ON invoice.customer_id = customer.customer_id
GROUP BY invoice.customer_id, customer.first_name, customer.last_name, customer.country
ORDER BY TotalSpent DESC
Limit 10;

    -- Group Customers by number of invoices
SELECT customer.customer_id, 
       customer.first_name || ' ' || customer.last_name AS CustomerName, 
       COUNT(invoice.invoice_id) AS NumberOfInvoices
FROM customer
LEFT JOIN invoice ON customer.customer_id = invoice.customer_id
GROUP BY customer.customer_id, customer.first_name, customer.last_name
ORDER BY NumberOfInvoices DESC
LIMIT 10;

    -- Identify each customer's perferred genre
SELECT customer.customer_id, 
       customer.first_name || ' ' || customer.last_name AS CustomerName, 
       genre.name AS PreferredGenre,
       COUNT(invoice_line.track_id) AS GenreCount
FROM customer
JOIN invoice ON customer.customer_id = invoice.customer_id
JOIN invoice_line ON invoice.invoice_id = invoice_line.invoice_id
JOIN track ON invoice_line.track_id = track.track_id
JOIN genre ON track.genre_id = genre.genre_id
GROUP BY customer.customer_id, genre.genre_id
ORDER BY GenreCount DESC
LIMIT 10;

-- 2. Product Popularity (Tracks and Albums) and Sales Trends

    -- Find top 10 tracks by sales.

    -- Revenue trends by album release date.

    -- Most popular genres per region.
 