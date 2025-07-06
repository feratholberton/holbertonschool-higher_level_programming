#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def states(username, userPassword, database_name):
    """Retrieve all states."""

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=userPassword, db=database_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()

    db.close()


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    bd = sys.argv[3]

    states(user, passw, bd)
