#!/usr/bin/python3
"Defines TestState class"
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    "Unittests for State class"

    def setUp(self):
        "Set up test cases."
        self.state = State()

    def tearDown(self):
        del self.state

    def test_state_inherits_from_BaseModel(self):
        "Test if State inherits from BaseModel."
        self.assertTrue(isinstance(self.state, BaseModel))

    def test_state_has_BaseModel_attributes(self):
        "Test if State has BaseModel's attributes."
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_class_attributes(self):
        "Checks if State has the required attributes."
        self.assertEqual(self.state.name, '')

    def test_init_attribues(self):
        "Inisialize the attributes."
        self.state.name = 'Casablanca'
        self.assertEqual(self.state.name, 'Casablanca')


if __name__ == '__main__':
    unittest.main()
