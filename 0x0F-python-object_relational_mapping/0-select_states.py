#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
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

    # Execute the SQL query to select all states and order by states.id
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all the rows as a list of tuples
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
