SELECT odate, snum, MAX(amt) AS largest_order
FROM Orders
WHERE amt > 3000
GROUP BY odate, snum
ORDER BY odate, snum;
