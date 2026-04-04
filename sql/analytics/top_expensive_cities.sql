SELECT 
    l.state, 
    l.city, 
    ROUND(AVG(f.price), 2) as avg_price,
    COUNT(f.location_id) as sales_volume
FROM fact_sales f
JOIN dim_location l ON f.location_id = l.location_id
GROUP BY l.state, l.city
HAVING sales_volume > 2
ORDER BY avg_price DESC 
LIMIT 10