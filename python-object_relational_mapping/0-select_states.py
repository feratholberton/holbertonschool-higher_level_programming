#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def states(mysql_username, mysql_password, database_name):
    """Get all states"""

    database = MySQLdb.connect(
        host="localhost", 
        port=3306,
        username=mysql_username, 
        password=mysql_password,
        database=database_name
    )

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    states(username, password, database)
