#!/usr/bin/python3

"""Import unit test, json, sys, and the Base class."""
import unittest
import json
import sys

pathh = '/alx-higher_level_programming/0x0C-python-almost_a_circle/models'
sys.path.append(pathh)
from base import Base


"""Test Base."""


class testBase(unittest.TestCase):
    """Test base."""

    def test_init(self):
        """Test Base's __init__ method."""
        # 21 can you do sumn for me?
        bbase = Base(id=21)
        self.assertEqual(bbase.id, 21)
        self.assertEqual(Base._Base__nb_objects, 0)

        secondBbase = Base()
        self.assertEqual(secondBbase.id, 1)

        thirdBbase = Base()
        fourthBbase = Base()
        self.assertEqual(fourthBbase.id, 3)

    def test_toJSON(self):
        """Test Base's to_json_string static method."""
        tester = []
        self.assertEqual(Base.to_json_string(tester), "[]")

        tester = [{
            "name": "Reaaal Bad Man",
            "occupation": "Works at a hair salon",
            "alter_ego": "Anita Max WyNn",
            "is_Everything_going_to_be_alright?": "Chupapi Mugagno"
        }, {
            "name": "Jenny",
            "id": 123,
            "DOB": "February 2nd 2022"
        }]

        test1test2test3 = Base.to_json_string(tester)
        whatWeShouldGet = json.dumps(tester)

        self.assertEqual(test1test2test3, whatWeShouldGet)

    def test_fromJSON(self):
        """Test Base's from_json_string static method."""
        maintest = Base.from_json_string(None)
        self.assertEqual(maintest, [])

        tester = '[{"name": "Sara", "age": 24}, {"name": "Yosan", "age": 23}]'
        maintest = Base.from_json_string(tester)
        whatWeShouldGet = [
            {"name": "Sara", "age": 24},
            {"name": "Yosan", "age": 23}
        ]
        self.assertEqual(maintest, whatWeShouldGet)
