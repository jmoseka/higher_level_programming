#!/usr/bin/python3
"""tests rectangle class"""

import unittest
import pep8
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Rectangle_Tests(unittest.TestCase):
    """test for Rectangle class"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_R_integer_width(self):
        """integer validator"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("10", 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(10.1, 2)

    def test_R_integer_height(self):
        """integer validator"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(2, 0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, {})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, 10.1)

    def test_R_integer_x(self):
        """integer validator"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 3, "2", 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(10, 3, -2, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 3, {}, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 3, 2.1, 1)

    def test_R_integer_y(self):
        """integer validator"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 3, 2, "1")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(10, 3, 2, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 3, 2, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 3, 2, 1.1)

    def test_R_area(self):
        """check area value"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_R_display(self):
        """check display a rectangle"""
        pass

    def test_R_str_(self):
        """check __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        string = str(r1)
        self.assertEqual(string, "[Rectangle] (12) 2/1 - 4/6")

    def test_R_Update_args(self):
        """check updating class"""
        pass

    def test_R_Update_kwargs(self):
        """check updating class"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(size=1)
        up = str(r1)
        self.assertNotEqual(up, "[Rectangle] (1) 10/10 - 10/1")

    def test_to_dictionary(self):
        """check updating class that returns a dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertTrue(r1_dictionary, dict)
