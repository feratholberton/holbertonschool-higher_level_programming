#!/usr/bin/python3
"""States via SQLAlchemy"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State


def addLouisiana(user_name, user_password, database_name):
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user_name, user_password, database_name))

    session = Session(engine)

    state = session.query(State).filter(State.id == '2').first()

    if state:
        state.name = 'New Mexico'
        session.commit()

    session.close()


if __name__ == '__main__':
    user_name = argv[1]
    user_password = argv[2]
    database_name = argv[3]

    addLouisiana(user_name, user_password, database_name)
