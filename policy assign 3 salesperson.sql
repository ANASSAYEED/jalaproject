SELECT 
    a.cname AS customer1, 
    b.cname AS customer2, 
    c.cname AS customer3,
    a.rating 
FROM 
    cust a
JOIN 
    cust b ON a.rating = b.rating AND a.cnum < b.cnum  -- Avoids duplicates (a, b) and (b, a)
JOIN 
    cust c ON a.rating = c.rating AND a.cnum < c.cnum AND b.cnum < c.cnum  -- Ensures all three customers have the same rating
ORDER BY 
    a.rating;
