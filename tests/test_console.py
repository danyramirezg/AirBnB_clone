#!/usr/bin/python3
"""Unittest cases for console"""

import unittest
import console
import pep8


class Test_BaseModel(unittest.TestCase):
    """Class for testing the console."""
    def test_pep8_console(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")
