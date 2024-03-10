#!/usr/bin/python3
"""
This module is for the unittest of the BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test case for the city class
    """
    
    def test_inheritance(self):
        """
        Test if city inherits from BaseModel class
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
        Test if the city has attributes
        """
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_initialization(self):
        """
        Test if City is properly initialized 
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
