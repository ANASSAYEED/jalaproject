WITH HighestTotalDay AS (
    SELECT odate, SUM(amt) AS total_amount
    FROM Orders
    GROUP BY odate
    ORDER BY total_amount DESC
    LIMIT 1
)
SELECT o.odate, o.snum, o.cnum, o.amt
FROM Orders o
JOIN HighestTotalDay htd ON o.odate = htd.odate;
