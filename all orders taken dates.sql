SELECT * 
FROM orders 
WHERE odate IN (TO_DATE('03-OCT-94', 'DD-MON-YY'), TO_DATE('04-OCT-94', 'DD-MON-YY'));

SELECT * 
FROM orders 
WHERE odate IN ('1994-10-03', '1994-10-04');
