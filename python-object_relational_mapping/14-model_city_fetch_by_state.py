#!/usr/bin/python3
"""States via SQLAlchemy"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State
from model_city import City


def deleteState(user_name, user_password, database_name):
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user_name, user_password, database_name))

    session = Session(engine)

    for city, state in (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id).all()
    ):

        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    user_name = argv[1]
    user_password = argv[2]
    database_name = argv[3]

    deleteState(user_name, user_password, database_name)
