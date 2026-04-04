SELECT 
    d.sale_year, 
    d.sale_quarter, 
    COUNT(*) as total_transactions,
    ROUND(SUM(f.price), 2) as total_revenue
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.sale_year, d.sale_quarter
ORDER BY d.sale_year DESC, d.sale_quarter DESC