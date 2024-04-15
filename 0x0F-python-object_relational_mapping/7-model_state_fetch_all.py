#!/usr/bin/python3

"""Import statements."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Session

if "__name__" == "__main__":
    theUsername = sys.argv[1]
    thePassword = sys.argv[2]
    theDatabase = sys.arg[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(theUsername, thePassword,
                                   theDatabase), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    sesh = Session(engine)

    for stateObj in sesh.query(State).order_by(State.id).all():
        print(stateObj.id + ": " + stateObj.name)
    sesh.close()
