-- Prints the full description of the table first_table
SELECT TABLE_NAME, CREATE_TABLE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'database_name'
AND TABLE_NAME = 'first_table';
