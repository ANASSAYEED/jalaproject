SELECT 
    onum, 
    snum, 
    amt, 
    amt * 0.12 AS commission
FROM orders
ORDER BY snum;
