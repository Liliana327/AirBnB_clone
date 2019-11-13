#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import pep8
import os
import time
# BaseModel = models.base_model.BaseModel
class TestBaseModel(unittest.TestCase):
    """Tests to check the documentation acnd style of BaseModel class"""
    def test_setUp(self):
        """SetUps tests"""
        try:
            os.remove("file.json")
        except:
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
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")
    def test_pep8_tests_base(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")
    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)

