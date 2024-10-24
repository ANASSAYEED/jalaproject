SELECT 'For ' || TO_CHAR(odate, 'dd/mm/yy') || ' there are ' || COUNT(*) || ' Orders' AS order_summary
FROM orders
GROUP BY odate;
