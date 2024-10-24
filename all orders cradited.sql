SELECT a.onum, b.sname, c.cname, a.amt
FROM orders a
JOIN salespeople b ON a.snum = b.snum
JOIN cust c ON a.cnum = c.cnum
WHERE a.snum = (SELECT snum FROM cust WHERE cname = 'Hoffman');
