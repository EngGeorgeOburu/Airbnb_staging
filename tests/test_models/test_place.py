#!/usr/bin/python3
"""
This is a unittest for the base model classs
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Class for unittessting
    """

    my_obj = Place()
    

    def setUp(self):
        """
        Setting up initial variables
        """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def test_places(self):
        """
        Test case for normal places 
        """
        obj = Place()
        obj.name = 'Nairobi'
        obj.number = 43
        obj.save()
        obj_dict = obj.to_dict()
        self.assertEqual(obj.name, "Nairobi")
        self.assertEqual(obj.number, 43)
        self.assertEqual(isinstance(obj.created_at, datetime), True)
        self.assertEqual(isinstance(obj.updated_at, datetime), True)

    def test_inheritance(self):
        """
        Test if class inherits from BaseModel
        """
        self.assertEqual(issubclass(Place, BaseModel), True)

    def test_attributes(self):
        """
        Test for the object attributes
        """
        self.assertEqual(type(self.place_obj.city_id), str)
        self.assertEqual(type(self.place_obj.user_id), str)
        self.assertEqual(type(self.place_obj.name), str)
        self.assertEqual(type(self.place_obj.description), str)
        self.assertEqual(type(self.place_obj.number_rooms), int)
        self.assertEqual(type(self.place_obj.number_bathrooms), int)
        self.assertEqual(type(self.place_obj.max_guest), int)
        self.assertEqual(type(self.place_obj.price_by_night), int)
        self.assertEqual(type(self.place_obj.latitude), float)
        self.assertEqual(type(self.place_obj.longitude), float)
        self.assertEqual(type(self.place_obj.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
