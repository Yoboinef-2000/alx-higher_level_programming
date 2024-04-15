#!/usr/bin/python3

"""Import statements."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
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

    cities = sesh.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    sesh.close()
