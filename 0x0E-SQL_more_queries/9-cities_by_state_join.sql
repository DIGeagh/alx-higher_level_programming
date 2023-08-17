-- Use the specified database
USE <database_name>;

-- List cities with required information and sorting
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
