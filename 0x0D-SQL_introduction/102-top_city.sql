-- Displays the top 3 cities' temperature during July and August ordered by temperature (descending)
SELECT city, AVG(temp_avgf) AS avg_temp
FROM temperatures
WHERE (date BETWEEN '2022-07-01' AND '2022-08-31')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
