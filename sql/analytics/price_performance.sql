SELECT 
    p.property_size_category, 
    ROUND(AVG(f.price_per_sqft), 2) as avg_sqft_price,
    ROUND(AVG(f.house_size), 2) as avg_house_size
FROM fact_sales f
JOIN dim_property p ON f.property_id = p.property_id
GROUP BY p.property_size_category
ORDER BY avg_sqft_price DESC