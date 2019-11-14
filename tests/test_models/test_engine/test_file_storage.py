#!/usr/bin/python3
"""File Storage Unit Tests"""

import models
import pep8
import unittest
from models import storage
from models import FileStorage


class Test_FileStorage(unittest.TestCase):
    """
    Test Cases for class
    """
    def test_docstrings(self):
        """Checks if docstring exist"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)

    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage_temp = FileStorage()
        new_dict = storage_temp.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage_temp._FileStorage.__objects)

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage_temp = FileStorage()
        new_dict = storage_temp.all()
        pancho = User()
        pancho.id = 2000
        pancho.name = "Gato"
        storage_temp.new(pancho)
        class_name = pancho.__class__.__name__
        key = "{}.{}".format(class_name, str(Holberton.id))
        self.assertIsNotNone(storage_temp[key])

    def test_attributes(self):
        """Test the attributes for FileStorage class"""
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))
        self.assertTrue(isinstance(storage._FileStorage__file_path, dict))

    def test_reload(self):
        """Tests the reaload method """
        JohnLen = FileStorage()
        sizeofobj = len(JohnLen._FileStorage.__objects)
        self.assertGreater(sizeofobj, 0)
