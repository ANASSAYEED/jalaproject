SELECT cnum, MIN(amt) AS smallest_order
FROM Orders
GROUP BY cnum;
