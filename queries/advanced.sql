SELECT 
    Category,
    SUM(Sales) AS sales,
    SUM(Profit) AS profit
FROM sales
GROUP BY Category
ORDER BY profit DESC;