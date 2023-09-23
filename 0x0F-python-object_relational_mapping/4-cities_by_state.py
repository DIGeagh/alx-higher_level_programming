#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Create a connection to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to select all cities and order by cities.id
        cursor.execute("SELECT * FROM cities ORDER BY id")

        # Fetch all the rows as a list of tuples
        cities = cursor.fetchall()

        # Print the results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()
