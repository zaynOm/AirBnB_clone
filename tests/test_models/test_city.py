#!/usr/bin/python3
"Defines TestCity class"
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    "Unittests for City class"

    def setUp(self):
        "Set up test cases."
        self.city = City()

    def tearDown(self):
        del self.city

    def test_state_inherits_from_BaseModel(self):
        "Test if City inherits from BaseModel."
        self.assertTrue(isinstance(self.city, BaseModel))

    def test_state_has_BaseModel_attributes(self):
        "Test if City has BaseModel's attributes."
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_class_attributes(self):
        "Checks if City has the required attributes."
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')

    def test_init_attribues(self):
        "Inisialize the attributes."
        self.city.name = 'rabat'
        self.city.state_id = 'my_state.12233'
        self.assertEqual(self.city.name, 'rabat')
        self.assertEqual(self.city.state_id, 'my_state.12233')


if __name__ == '__main__':
    unittest.main()
