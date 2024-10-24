SELECT 
    s.sname, 
    o.amt * s.comm AS commission_amount
FROM 
    orders o
JOIN 
    cust c ON o.cnum = c.cnum
JOIN 
    salespeople s ON c.snum = s.snum
WHERE 
    c.rating > 100;
