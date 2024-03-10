#!/usr/bin/python3
"""
Unittest for the amenity base model class.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from models import storage

class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """


    def tes_init(self):
        """
        Test the initialization of the instance of amenity class
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_init_arg(self):
        """
        Testing initialization of the amenity instance with arguements
        """
        amenity = Amenity(name = "Testing Amenity")
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "Testing Amenity"_)

    def test_inheritance(self):
        """
        Test if the Amenity class inherits from the parent class
        Base Model
        """
        amenity = Amenity()
        self.assertTrue(issubclass(amenity, BaseModel))

    def test_for_attributes(self):
        """
        Testing attributes for Amenity instance
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

    def test_to_dictionary(self):
        """
        Testing the to_dict of the Amenity class
        """
        amenity = Amenity(name, "Testing Amenity")
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Testing Amenity')

    def test_str_representation(self):
        """
        Testing the __str__method of Amenityinstance. 
        """
        amenity = Amenity(name = "Testing Amenity")
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity__dict__))

if __name__ == '__main__':
    unittest.main()
