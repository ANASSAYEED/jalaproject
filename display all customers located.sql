SELECT 
    c.cname 
FROM 
    cust c 
WHERE 
    c.city IN (SELECT DISTINCT c2.city 
                FROM cust c2 
                JOIN salespeople s ON c2.snum = s.snum 
                WHERE s.sname = 'Serres')
ORDER BY 
    c.cname;
