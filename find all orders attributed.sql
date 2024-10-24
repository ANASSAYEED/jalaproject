SELECT o.onum, o.snum, o.cnum, o.amt, o.odate
FROM orders o
JOIN cust c ON o.cnum = c.cnum
JOIN salespeople s ON o.snum = s.snum
WHERE c.city = 'London';
