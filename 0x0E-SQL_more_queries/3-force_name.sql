USE <database_name>;

-- Create table force_name if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

-- Describe the table to verify its structure
DESCRIBE force_name;
