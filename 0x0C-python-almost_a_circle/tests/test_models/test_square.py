#!/usr/bin/python3
"""test Square class"""

import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Square_Tests(unittest.TestCase):
    """tests Square class"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_S_integer_size(self):
        """integer validator"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square("10")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(-10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square({})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(10.1)

    def test_S_integer_x(self):
        """integer validator"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(10, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(10, -2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(10, {})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(10, 2.1)

    def test_S_integer_y(self):
        """integer validator"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 3, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(10, 3, -2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 3, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 3, 2.1,)
