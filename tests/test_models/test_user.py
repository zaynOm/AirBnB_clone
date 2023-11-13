#!/usr/bin/python3
"Defines TestUser class"
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    "Unittests for User class"

    def setUp(self):
        "Set up test cases."
        self.user = User()

    def tearDown(self):
        del self.user

    def test_user_inherits_from_BaseModel(self):
        "Test if User inherits from BaseModel."
        self.assertTrue(isinstance(self.user, BaseModel))

    def test_user_has_BaseModel_attributes(self):
        "Test if User has BaseModel's attributes."
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_class_attributes(self):
        "Checks if User has the required attributes."
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_init_attribues(self):
        "Inisialize the attributes."
        self.user.email = 'hbnb@mail.com'
        self.user.password = '1234'
        self.user.first_name = 'Zayn'
        self.user.last_name = 'Om'

        self.assertEqual(self.user.email, 'hbnb@mail.com')
        self.assertEqual(self.user.password, '1234')
        self.assertEqual(self.user.first_name, 'Zayn')
        self.assertEqual(self.user.last_name, 'Om')


if __name__ == '__main__':
    unittest.main()
