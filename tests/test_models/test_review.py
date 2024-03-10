#!/usr/bin/python3
"""
Module for testing BaseModel
"""
import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Test cases for the Review class
    """
    
    def test_inheritance(self):
        """
        Testing if the Review inherits from the BaseModel
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """
        Test if attributes are properly initialized to empty strings
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes_assignment(self):
        """
        Test if attributes can be assigned correctly
        """
        review = Review()
        review.place_id = "place_id_123"
        review.user_id = "user_id_450"
        review.text = "This is a review text"
        self.assertEqual(review.place_id, "place_id_123")
        self.assertEqual(review.user_id, "user_id_456")
        self.assertEqual(review.text, "This is a review text")

    def test_to_dict_method(self):
        """
        Test if to_dict() method returnsthe expected dictionary
        """
        review = Review()
        review.place_id = "place_id_123"
        review.user_id = "user_id_456"
        review.text = "This is a review text"
        review_dict = review.to_dict()
        expected_dict = {
                '__class__': 'Review',
                'id': review.id,
                'created_at': review.created_at.isoformat(),
                'updated_at': review.updated_at.isoformat(),
                'place_id': "place_id_123",
                'user_id': "user_id_456",
                'text': "This is a review text"
                }
        self.assertDictEqual(review_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
