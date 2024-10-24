SELECT 
    c.cname, 
    s.sname, 
    s.comm 
FROM 
    cust c
JOIN 
    salespeople s ON c.snum = s.snum
WHERE 
    s.comm > 0.12;