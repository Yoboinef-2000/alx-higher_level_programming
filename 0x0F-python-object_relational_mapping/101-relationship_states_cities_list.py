#!/usr/bin/python3

"""Import statements."""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import Session

if __name__ == "__main__":
    theUsername = sys.argv[1]
    thePassword = sys.argv[2]
    theDatabase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(theUsername, thePassword,
                                   theDatabase))

    Base.metadata.create_all(engine)
    sesh = Session(engine)

    statesCities = sesh.query(State).order_by(State.id).all()
    for state in statesCities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    sesh.close()
