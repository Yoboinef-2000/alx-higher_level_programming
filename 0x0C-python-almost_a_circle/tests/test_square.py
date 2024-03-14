#!/usr/bin/python3

"""Import unit test, sys, and the Sqaure class."""
import unittest
import sys

pathh = '/alx-higher_level_programming/0x0C-python-almost_a_circle/models'
sys.path.append(pathh)
from square import Square


"""Test Sqaure."""


class testSquare(unittest.TestCase):
    """Test Square."""

    def test_inheritance(self):
        """Test for inheritance."""
        from base import Base
        from rectangle import Rectangle
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_init(self):
        """Test Sqaure's __init__ method."""
        ssquare = Square(9, 11, 12, 13)
        self.assertEqual(ssquare.id, 13)
        self.assertEqual(ssquare.size, 9)
        self.assertEqual(ssquare.x, 11)
        self.assertEqual(ssquare.y, 12)

        # Giving size only
        ssquare2 = Square(27)
        self.assertEqual(ssquare2.id, 1)
        self.assertEqual(ssquare2.size, 27)
        self.assertEqual(ssquare2.x, 0)
        self.assertEqual(ssquare2.y, 0)

    def test_area(self):
        """Test the area of a Sqaure."""
        ssquare = Square(12345, 11, 12, 13)
        self.assertEqual(ssquare.area(), 152399025)

        ssquare.size = 27
        self.assertEqual(ssquare.area(), 729)

    def test_gettersAndSetters(self):
        """Test Square's getters and setters."""
        ssquare = Square(14, 11, 12, 13)

        ssquare.size = 89
        self.assertEqual(ssquare.size, 89)
        with self.assertRaises(ValueError):
            ssquare.size = 0
        with self.assertRaises(TypeError):
            ssquare.size = "Told my doctor"

        ssquare.x = 823
        self.assertEqual(ssquare.x, 823)
        with self.assertRaises(ValueError):
            ssquare.x = -1
        with self.assertRaises(TypeError):
            ssquare.x = "I am a healthy kid"

        ssquare.y = 90
        self.assertEqual(ssquare.y, 90)
        with self.assertRaises(ValueError):
            ssquare.y = -1
        with self.assertRaises(TypeError):
            ssquare.y = "I smoke Broccoli. :)"

    def test_str(self):
        """Test Square's __str__ method."""
        ssquare = Square(2, 4, 5, 12)
        self.assertEqual(ssquare.__str__(), "[Square] (12) 4/5 - 2")

        ssquare2 = Square(10, 2, 1)
        self.assertEqual(ssquare2.__str__(), "[Square] (2) 2/1 - 10")

    def test_display(self):
        """Test the Square's display method."""
        from io import StringIO
        import sys

        ssquare = Square(2, 2, 2, 12)

        thePrint = sys.stdout
        sys.stdout = StringIO()
        ssquare.display()
        mainPrint = sys.stdout.getvalue()
        sys.stdout = thePrint

        self.assertEqual(mainPrint, "\n\n  ##\n  ##\n")

    def test_update(self):
        """Test Rectangle's update method."""
        ssquare = Square(2, 3, 2, 12)
        ssquare.update(90, 123, 1, 47)
        self.assertEqual(ssquare.id, 90)
        self.assertEqual(ssquare.size, 123)
        self.assertEqual(ssquare.x, 1)
        self.assertEqual(ssquare.y, 47)

        ssquare.update(78)
        self.assertEqual(ssquare.id, 78)
        ssquare.update(78, 90)
        self.assertEqual(ssquare.size, 90)
        ssquare.update(78, 90, 15)
        self.assertEqual(ssquare.x, 15)
        ssquare.update(78, 90, 15, 14)
        self.assertEqual(ssquare.y, 14)

        ssquare.update(x=12, size=10)
        self.assertEqual(ssquare.id, 78)
        self.assertEqual(ssquare.size, 10)
        self.assertEqual(ssquare.x, 12)
        self.assertEqual(ssquare.y, 14)

        ssquare.update(17, 78, 89, 90, id=4, height=10, x=11)
        self.assertEqual(ssquare.id, 17)
        self.assertEqual(ssquare.size, 78)
        self.assertEqual(ssquare.x, 89)
        self.assertEqual(ssquare.y, 90)

    def test_toDictionary(self):
        """Test Rectangle's to_dictionary method."""
        ssquare = Square(2, 4, 5, 12)
        oP = {'x': 4, 'y': 5, 'id': 12, 'size': 2}
        self.assertEqual(ssquare.to_dictionary(), oP)
