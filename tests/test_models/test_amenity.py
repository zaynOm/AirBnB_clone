#!/usr/bin/python3
"Defines TestAmenity class"
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    "Unittests for Amenity class"

    def setUp(self):
        "Set up test cases."
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_state_inherits_from_BaseModel(self):
        "Test if Amenity inherits from BaseModel."
        self.assertTrue(isinstance(self.amenity, BaseModel))

    def test_state_has_BaseModel_attributes(self):
        "Test if Amenity has BaseModel's attributes."
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_class_attributes(self):
        "Checks if Amenity has the required attributes."
        self.assertEqual(self.amenity.name, '')

    def test_init_attribues(self):
        "Inisialize the attributes."
        self.amenity.name = 'Fitness Center'
        self.assertEqual(self.amenity.name, 'Fitness Center')


if __name__ == '__main__':
    unittest.main()
