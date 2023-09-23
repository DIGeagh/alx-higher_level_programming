#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Create a connection to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
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

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()
