#!/usr/bin/python3

"""Import sqlalchemy and some of its moduels with in."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
"""Class State."""


class State(Base):
    """Class State."""

    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
