#!/usr/bin/python3
"""test Base class"""

import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Base_Tests(unittest.TestCase):
    """tests for Base class"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def Test_BaseMethods(self):
        """check for methods"""
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)

    def test_BaseId(self):
        """checks for a new object id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(-2)
        self.assertEqual(b2.id, -2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base("four")
        self.assertEqual(b4.id, "four")
        b5 = Base([1, 2])
        self.assertEqual(b5.id, [1, 2])

    def test_to_json(self):
        """test to_json string task"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dicti = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dict = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        """test save_to_file task"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile('Rectangle.json'))

    def test_from_json(self):
        """Tests from_json_string task"""
        st_in = '[{"id": 89, "width": 10, "height": 4},\
{"id": 7, "width": 1, "height": 7}]'
        empty_ls = []
        st_out = Rectangle.from_json_string(st_in)
        self.assertEqual(len(st_out), 2)
