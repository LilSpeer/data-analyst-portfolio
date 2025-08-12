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

-- 2. Revenue Analysis and Trends

    -- Average Revenue Trends for each Day of the Week
SELECT 
    CASE strftime('%w', invoice.invoice_date)
        WHEN '0' THEN 'Sunday'
        WHEN '1' THEN 'Monday'
        WHEN '2' THEN 'Tuesday'
        WHEN '3' THEN 'Wednesday'
        WHEN '4' THEN 'Thursday'
        WHEN '5' THEN 'Friday'
        WHEN '6' THEN 'Saturday'
    END AS day_of_week,
    ROUND(AVG(total), 2) as avg_daily_gross_revenue
FROM invoice
GROUP BY CAST(strftime('%w', invoice_date) AS INTEGER)
ORDER BY CAST(strftime('%w', invoice_date) AS INTEGER);

    -- Monthly Revenue Trends
SELECT strftime('%Y-%m', invoice.invoice_date) AS sale_month,
       ROUND(SUM(invoice.total), 2) AS monthly_gross_revenue
FROM invoice
GROUP BY sale_month
ORDER BY sale_month;

    -- Yearly Revenue Trends
SELECT strftime('%Y', invoice.invoice_date) AS sale_year, 
       ROUND(SUM(invoice.total), 2) AS yearly_gross_revenue
FROM invoice
GROUP BY sale_year 
ORDER BY sale_year;

    -- Revenue Trends by Country
SELECT customer.country, 
       ROUND(SUM(invoice.total), 2) AS country_gross_revenue
FROM invoice
JOIN customer ON invoice.customer_id = customer.customer_id
GROUP BY customer.country
ORDER BY country_gross_revenue DESC;

    -- Average Order Value (AOV) by Customer (Top 20)
SELECT customer.customer_id, 
       customer.first_name || ' ' || customer.last_name AS CustomerName, 
       ROUND(AVG(invoice.total), 2) AS avg_order_value,
       COUNT(invoice.invoice_id) AS order_count
FROM customer
JOIN invoice ON customer.customer_id = invoice.customer_id
GROUP BY customer.customer_id, customer.first_name, customer.last_name
ORDER BY avg_order_value DESC
LIMIT 20;

-- 3. Employee Performance Analysis

    -- Employees who manage the most customers
SELECT employee.employee_id, 
       employee.first_name || ' ' || employee.last_name AS EmployeeName, 
       COUNT(customer.customer_id) AS num_customers
FROM employee
JOIN customer ON employee.employee_id = customer.support_rep_id
GROUP BY employee.employee_id, employee.first_name, employee.last_name
ORDER BY num_customers DESC;


-- 4. Customer Analysis

    -- Top 5 Customers Each Month by Revenue
WITH monthly_spending AS (
    SELECT 
        c.customer_id, c.first_name,c.last_name,strftime('%Y-%m', i.invoice_date) AS month, ROUND(SUM(i.total),2) AS monthly_total
    FROM invoice i
    JOIN customer c ON i.customer_id = c.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name, month      
),
customers_ranked AS (
    SELECT customer_id, first_name, last_name, month, monthly_total,
        RANK() OVER (PARTITION BY month ORDER BY monthly_total DESC) AS rank
    FROM monthly_spending
)
SELECT customer_id, first_name, last_name, month, monthly_total
FROM customers_ranked
WHERE rank <= 5;

    -- Customer Lifetime Value (CLV) Estimation
SELECT customer_id,
    ROUND(SUM(total),2) AS lifetime_value, COUNT(invoice_id) AS purchase_count, ROUND(AVG(total),2) AS avg_purchase_value
FROM invoice
GROUP BY customer_id
ORDER BY lifetime_value DESC;

    -- Customer Retention and Churn Analysis
WITH first_purchase AS (
    SELECT customer_id, MIN(strftime('%Y-%m', invoice_date)) AS cohort_month
    FROM invoice
    GROUP BY customer_id
),
purchases AS (
    SELECT customer_id, strftime('%Y-%m', invoice_date) AS purchase_month
    FROM invoice
)
SELECT
    f.cohort_month,
    p.purchase_month,
    COUNT(DISTINCT p.customer_id) AS retained_customers,
    (CAST(substr(p.purchase_month, 1, 4) AS INTEGER) * 12 + CAST(substr(p.purchase_month, 6, 2) AS INTEGER)) -
    (CAST(substr(f.cohort_month, 1, 4) AS INTEGER) * 12 + CAST(substr(f.cohort_month, 6, 2) AS INTEGER)) AS months_since_first_purchase
FROM first_purchase f
JOIN purchases p ON f.customer_id = p.customer_id
GROUP BY f.cohort_month, p.purchase_month
ORDER BY f.cohort_month, p.purchase_month;

    -- Identify Customers with Cross-Genre Purchases (more than 5 genres)
SELECT c.customer_id, c.first_name || ' ' || c.last_name AS customer_name, COUNT(DISTINCT g.genre_id) AS genre_count
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
JOIN invoice_line il ON i.invoice_id = il.invoice_id
JOIN track t ON il.track_id = t.track_id
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY c.customer_id
HAVING genre_count > 5;




 