#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for state class
    """
    
    def test_inheritance (self):
        """
        Test if state inherits from the BaseModel
        """
        state_instance = State()
        self.assertIsInstance(state_instance, BaseModel)

    def test_attributes(self):
        """"
        Test if state isattributes are initialized to aan emoty string
        """
        state_instance = State()
        self.assertEqual(state_instance.state, "")

    def test_attributes_assignment(self):
        """
        Test if state attributes can be assigned correctly
        """
        state_instance = State()
        state_instance.state = "California"
        self.assertEqual(state_instance.state, "California")

    def test_t0_dict_method(self):
        """
        Test if to_dict method returns the expected dictionary
        """
        state.instance = State()
        state_instance.state = "California"
        state_dict = state_instance.to_dict()
        expected_dict = {
                '__class__': 'State',
                'id': state_instance.id,
                'created_at': state_instance.created_at.isoformat(),
                'updated_at': state_instance.updated_at.isoformat(),
                'state': "California"
                }
        self.assertDictEqual(state_dict, expected_dict)


if __name__ = '__main__':
    unittest.main()

