-- This script displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(temperature * 9/5 + 32) AS average_temperature_fahrenheit
FROM your_table_name
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
