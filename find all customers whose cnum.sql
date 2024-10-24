SELECT cnum, cname
FROM cust
WHERE cnum = (SELECT snum + 1000 FROM salespeople WHERE sname = 'Serres');
