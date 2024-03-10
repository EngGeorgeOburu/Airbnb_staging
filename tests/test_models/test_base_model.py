#!/usr/bin/python3
"""
Unit test for BaseModul class
"""

import unittest
from datetime import datetime
from models import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """
        Set up the testing environment
        """
        self.base_model = BaseModel()

    def test_instance_creation(self):
        """
        Test if an instance of the BaseModel is created 
        """
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id_generation(self):
        """
        Test if an ID is generated
        """
        self.assertIsNotNone(self.base_model.id)

    def test_updated_at(self):
        """
        Test if updated_at is attribute is a datetime object
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_created_at(self):
        """
        Test if created at is attribute of datetime object
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_save_method(self):
        """
        Test if save method updates at updated_at 
        """
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test if to_dict method returns a dictionary with expected keys
        """
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
