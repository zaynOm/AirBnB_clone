#!/usr/bin/python3
"Defines TestReview class"
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    "Unittests for Review class"

    def setUp(self):
        "Set up test cases."
        self.review = Review()

    def tearDown(self):
        del self.review

    def test_state_inherits_from_BaseModel(self):
        "Test if Review inherits from BaseModel."
        self.assertTrue(isinstance(self.review, BaseModel))

    def test_state_has_BaseModel_attributes(self):
        "Test if Review has BaseModel's attributes."
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_class_attributes(self):
        "Checks if Review has the required attributes."
        self.assertEqual(self.review.text, '')
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')

    def test_init_attribues(self):
        "Inisialize the attributes."
        self.review.text = 'I love this place.'
        self.review.place_id = 'hot.12233'
        self.review.user_id = 'user.12233'

        self.assertEqual(self.review.text, 'I love this place.')
        self.assertEqual(self.review.place_id, 'hot.12233')
        self.assertEqual(self.review.user_id, 'user.12233')


if __name__ == '__main__':
    unittest.main()
