#!/usr/bin/python3

"""Import unit test, sys,  and the Rectangle class."""
import unittest
import sys

pathh = '/alx-higher_level_programming/0x0C-python-almost_a_circle/models'
sys.path.append(pathh)
from rectangle import Rectangle


"""Test Rectangle."""


class testRectangle(unittest.TestCase):
    """Test Rectangle."""

    def test_inheritance(self):
        """Test for inheritance."""
        from base import Base
        self.assertTrue(issubclass(Rectangle, Base))

    def test_init(self):
        """Test Rectangle's __init__ method."""
        rrectangle = Rectangle(9, 10, 11, 12, 13)
        self.assertEqual(rrectangle.id, 13)
        self.assertEqual(rrectangle.width, 9)
        self.assertEqual(rrectangle.height, 10)
        self.assertEqual(rrectangle.x, 11)
        self.assertEqual(rrectangle.y, 12)

        # Giving width and the height only
        rrectangle2 = Rectangle(27, 28)
        self.assertEqual(rrectangle2.id, 1)
        self.assertEqual(rrectangle2.width, 27)
        self.assertEqual(rrectangle2.height, 28)
        self.assertEqual(rrectangle2.x, 0)
        self.assertEqual(rrectangle2.y, 0)

    def test_gettersAndSetters(self):
        """Test Rectangle's getters and setters."""
        rrectangle = Rectangle(9, 10, 11, 12, 13)

        rrectangle.width = 89
        self.assertEqual(rrectangle.width, 89)
        with self.assertRaises(ValueError):
            rrectangle.width = 0
        with self.assertRaises(TypeError):
            rrectangle.width = "Yeah"

        rrectangle.height = 81234
        self.assertEqual(rrectangle.height, 81234)
        with self.assertRaises(ValueError):
            rrectangle.height = 0
        with self.assertRaises(TypeError):
            rrectangle.height = "they hatin"

        rrectangle.x = 823
        self.assertEqual(rrectangle.x, 823)
        with self.assertRaises(ValueError):
            rrectangle.x = -1
        with self.assertRaises(TypeError):
            rrectangle.x = "but they"

        rrectangle.y = 90
        self.assertEqual(rrectangle.y, 90)
        with self.assertRaises(ValueError):
            rrectangle.y = -1
        with self.assertRaises(TypeError):
            rrectangle.y = "broke tho"

    def test_area(self):
        """Test the area of a Rectangle."""
        rrectangle = Rectangle(9, 10, 11, 12, 13)
        self.assertEqual(rrectangle.area(), 90)

        rrectangle.width = 27
        rrectangle.height = 27
        self.assertEqual(rrectangle.area(), 729)

    def test_display(self):
        """Test the Rectangle's display method."""
        from io import StringIO
        import sys

        rrectangle = Rectangle(2, 3, 2, 2, 12)

        thePrint = sys.stdout
        sys.stdout = StringIO()
        rrectangle.display()
        mainPrint = sys.stdout.getvalue()
        sys.stdout = thePrint

        self.assertEqual(mainPrint, "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """Test Rectangle's __str__ method."""
        rrectangle = Rectangle(2, 3, 2, 2, 12)
        self.assertEqual(rrectangle.__str__(), "[Rectangle] (12) 2/2 - 2/3")

        rrectangle2 = Rectangle(5, 5, 1)
        self.assertEqual(rrectangle2.__str__(), "[Rectangle] (2) 1/0 - 5/5")

    def test_update(self):
        """Test Rectangle's update method."""
        rrectangle = Rectangle(2, 3, 2, 2, 12)
        rrectangle.update(90, 12, 123, 1, 47)
        self.assertEqual(rrectangle.id, 90)
        self.assertEqual(rrectangle.width, 12)
        self.assertEqual(rrectangle.height, 123)
        self.assertEqual(rrectangle.x, 1)
        self.assertEqual(rrectangle.y, 47)

        rrectangle.update(78)
        self.assertEqual(rrectangle.id, 78)
        rrectangle.update(78, 90)
        self.assertEqual(rrectangle.width, 90)
        rrectangle.update(78, 90, 15)
        self.assertEqual(rrectangle.height, 15)
        rrectangle.update(78, 90, 15, 14)
        self.assertEqual(rrectangle.x, 14)
        rrectangle.update(78, 90, 15, 14, 13)
        self.assertEqual(rrectangle.y, 13)

        rrectangle.update(x=12, height=10)
        self.assertEqual(rrectangle.id, 78)
        self.assertEqual(rrectangle.width, 90)
        self.assertEqual(rrectangle.height, 10)
        self.assertEqual(rrectangle.x, 12)
        self.assertEqual(rrectangle.y, 13)

        rrectangle.update(17, 12, 78, 89, 90, id=4, height=10, x=11)
        self.assertEqual(rrectangle.id, 17)
        self.assertEqual(rrectangle.width, 12)
        self.assertEqual(rrectangle.height, 78)
        self.assertEqual(rrectangle.x, 89)
        self.assertEqual(rrectangle.y, 90)

    def test_toDictionary(self):
        """Test Rectangle's to_dictionary method."""
        rrectangle = Rectangle(2, 3, 4, 5, 12)
        oP = {'x': 4, 'y': 5, 'id': 12, 'height': 3, 'width': 2}
        self.assertEqual(rrectangle.to_dictionary(), oP)
