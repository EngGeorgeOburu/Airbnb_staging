#!/usr/bin/python3
"""
Module for testing BaseModel
"""

import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test case for the User class
    """

    def test_inheritance(self):
        """
        Test if User inherits from BaseModel
        """
        user_instance = User()
        self.assertIsInstance(user_instance, BaseModel)

    def test_attributes(self):
        """
        Test if attributes initialized to empty strings
        """
        user_instance = User()
        self.assertEqual(user_instance.email, "")
        self.assertEqual(user_instance.password, "")
        self.assertEqual(user_instance.first_name, "")
        self.assertEqual(user_instance.last_name, "")

    def test_attribute_assignment(self):
        """
        Test if attributes can be assigned correctly
        """
        user_instance = User()
        user_instance.email = "george@oburu.com"
        user_instance.password = "pass12345"
        user_instance.first_name = "John"
        user_instance.last_name = "George"
        self.assertEqual(user_instance.email, "george@oburu.com")
        self.assertEqual(user_instance.password, "pass12345")
        self.assertEqual(user_instance.first_name, "John")
        self.assertEqual(user_instance.last_name, "George")

    def test_to_dict_method(self):
        """
        Test if t0_dict methd returns the expected dictionary
        """
        user_instance = User()
        user_instance.email = "george@oburu.com"
        user_instance.password = "pass12345"
        user_instance.first_name = "John"
        user_instance.last_name = "George"
        user_dict = user_instance.to_dict()
        expected_dict = {
                '__class__': 'User',
                'id': user_instance.id,
                'created_at': user_instance.created_at.isoformat(),
                'updated_at': user_instance.updated_at.isoformat(),
                'email': "george@oburu.com",
                'password': "pass12345",
                'first_name': "John",
                'last_name': "George"
                }
        self.assertDictEqual(user_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
