#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

        # Prepare the SQL query with a parameterized query to avoid SQL injection
        query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
        
        # Execute the SQL query with the state_name as a parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows as a list of tuples
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()
