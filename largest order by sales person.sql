SELECT snum, MAX(amt) AS largest_order
FROM Orders
GROUP BY snum
ORDER BY snum;
