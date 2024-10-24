SELECT 
    'For the city (' || city || '), the highest rating is : (' || MAX(rating) || ')' AS city_rating
FROM 
    cust
GROUP BY 
    city;
