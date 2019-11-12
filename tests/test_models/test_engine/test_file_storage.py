#!/usr/bin/python3
"""Unittest cases for file storage"""

import unittest
from models.engine.file_storage import FileStorage
import pep8
import os
import uuid


class Test_File_Storage(unittest.TestCase):
    """
    Class for testing File storage class.
    """

    # def test_setUp(self):
    #     """SetUps tests"""

    # def test_tearDown(self):
    #     """"Restart tests"""
    #     if os.path.exists(self.file_path):
    #         os.remove(self.file_path)
    #     if os.path.exists('new'):
    #         os.rename('new', self.file_path)

    def test_pep8_base_model(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_pep8_tests_base(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_isinstance(self):
        """Test the instance"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    # test reload, all, save
