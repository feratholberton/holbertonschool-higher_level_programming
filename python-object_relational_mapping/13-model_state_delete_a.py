#!/usr/bin/python3
"""States via SQLAlchemy"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State


def deleteState(user_name, user_password, database_name):
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user_name, user_password, database_name))

    session = Session(engine)

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()

    session.close()


if __name__ == '__main__':
    user_name = argv[1]
    user_password = argv[2]
    database_name = argv[3]

    deleteState(user_name, user_password, database_name)
