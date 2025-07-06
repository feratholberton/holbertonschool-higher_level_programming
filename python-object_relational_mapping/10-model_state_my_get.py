#!/usr/bin/python3
"""States via SQLAlchemy"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def stateName(user_name, user_password, database_name, state_name):
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user_name, user_password, database_name))

    session = Session(engine)

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print("{}".format(state.id))
    else:
        print('Not found')

    session.close()


if __name__ == '__main__':
    user_name = argv[1]
    user_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    stateName(user_name, user_password, database_name, state_name)
