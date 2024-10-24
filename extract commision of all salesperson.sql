SELECT s.sname, s.commission
FROM salespeople s
JOIN cust c ON s.snum = c.snum
WHERE c.city = 'London';
