SELECT 
    a.cname AS customer1, 
    b.cname AS customer2, 
    a.rating 
FROM 
    cust a
JOIN 
    cust b ON a.rating = b.rating 
WHERE 
    a.cnum != b.cnum;
