SELECT cname 
FROM cust, orders 
WHERE orders.cnum = cust.cnum 
  AND orders.snum IN (
    SELECT snum 
    FROM salespeople 
    WHERE sname IN ('Peel', 'Motika')
);
