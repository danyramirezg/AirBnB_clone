#!/usr/bin/python3
"""Unittest cases for Amenity"""

import unittest
from models.amenity import Amenity
import pep8
import os


class Test_Amenity(unittest.TestCase):
    """"Class Amenity -Unittest """

    def test_setUp(self):
        """SetUps tests"""
        pass

    def test_tearDown(self):
        """"Restart tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_base_model(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_pep8_tests_base(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_isinstance(self):
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_args(self):
        """Arguments to the instance"""
        b = Amenity(8)
        self.assertEqual(type(b).__name__, "Amenity")
        self.assertFalse(hasattr(b, "8"))

    # def test_str(self):
    #     """Prints correctly"""
    #     b = Amenity()
    #     printb = b.__str__()
    #     self.assertEqual(printb,
    #                      "[BaseModel] ({}) {}".format(b.id, b.__dict__))
