#!/usr/bin/python3
"Defines TestPlace class"
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    "Unittests for Place class"

    def setUp(self):
        "Set up test cases."
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_state_inherits_from_BaseModel(self):
        "Test if Place inherits from BaseModel."
        self.assertTrue(isinstance(self.place, BaseModel))

    def test_state_has_BaseModel_attributes(self):
        "Test if Place has BaseModel's attributes."
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_class_attributes(self):
        "Checks if Place has the required attributes."
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_init_attribues(self):
        "Inisialize the attributes."
        self.place.city_id = 'fes.1234'
        self.place.user_id = 'user.4455'
        self.place.name = 'hotelo'
        self.place.description = 'The best place'
        self.place.number_rooms = 5
        self.place.number_bathrooms = 3
        self.place.max_guest = 8
        self.place.price_by_night = 500
        self.place.latitude = 12.098
        self.place.longitude = 5.923
        self.place.amenity_ids = ['am1.99', 'am2.32']

        self.assertEqual(self.place.city_id, 'fes.1234')
        self.assertEqual(self.place.user_id, 'user.4455')
        self.assertEqual(self.place.name, 'hotelo')
        self.assertEqual(self.place.description, 'The best place')
        self.assertEqual(self.place.number_rooms, 5)
        self.assertEqual(self.place.number_bathrooms, 3)
        self.assertEqual(self.place.max_guest, 8)
        self.assertEqual(self.place.price_by_night, 500)
        self.assertEqual(self.place.latitude, 12.098)
        self.assertEqual(self.place.longitude, 5.923)
        self.assertEqual(self.place.amenity_ids, ['am1.99', 'am2.32'])


if __name__ == '__main__':
    unittest.main()
