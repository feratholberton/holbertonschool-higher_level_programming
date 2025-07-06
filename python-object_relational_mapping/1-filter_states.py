#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def states(user_name, user_password, database_name):
    """Filter states."""

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=user_password,
        db=database_name
    )

    cursor = database.cursor()
    cursor.execute(
        "SELECT * FROM states " +
        "WHERE BINARY name LIKE 'N%' " +
        "ORDER BY states.id"
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    bd = sys.argv[3]

    states(user, passw, bd)
