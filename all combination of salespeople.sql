SELECT 
    s.sname, 
    c.cname 
FROM 
    salespeople s
JOIN 
    cust c 
ON 
    s.city = c.city;
