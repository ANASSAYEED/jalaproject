SELECT 
    o.onum, 
    s.sname, 
    c.cname 
FROM 
    orders o
JOIN 
    cust c ON o.cnum = c.cnum
JOIN 
    salespeople s ON o.snum = s.snum;
