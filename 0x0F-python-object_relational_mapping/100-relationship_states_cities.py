#!/usr/bin/python3

"""Import statements."""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

"""Script that creates the State "California
   with the City "San Fransisco."""

if __name__ == "__main__":
    theUsername = sys.argv[1]
    thePassword = sys.argv[2]
    theDatabase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(theUsername, thePassword, theDatabase),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    sesh = Session(engine)

    cali = State(name='California')
    sanFran = City(name='San Francisco')
    cali.cities.append(sanFran)
    sesh.add(cali)
    sesh.add(sanFran)
    sesh.commit()

    sesh.close()
