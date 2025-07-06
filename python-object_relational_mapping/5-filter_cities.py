#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def states(user_name, user_password, database_name, state_name):
    """Filter states."""

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=user_password,
        db=database_name
    )

    cursor = database.cursor()

    query = (
        "SELECT cities.name FROM cities " +
        "JOIN states ON cities.state_id = states.id " +
        "WHERE states.name LIKE %s ORDER BY cities.id"
    )

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    print(", ".join(city[0] for city in rows))

    cursor.close()
    database.close()


if __name__ == "__main__":
    user_name = sys.argv[1]
    user_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    states(user_name, user_password, database_name, state_name)
