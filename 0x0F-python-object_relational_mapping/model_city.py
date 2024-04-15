#!/usr/bin/python3

"""Import sqlalchemy and some of its moduels with in."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

"""Class State."""


class City(Base):
    """Class State."""

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
