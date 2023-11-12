#!/usr/bin/python3
"Defines TestBaseModel class"
from models.base_model import BaseModel
import unittest
import re
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    "Unittests for BaseModel class"

    def setUp(self):
        self.bm = BaseModel()

    def test_id_type(self):
        self.assertEqual(type(self.bm.id), str)

    def test_id_lenght(self):
        self.assertEqual(len(self.bm.id), 36)

    def test_id_format(self):
        self.assertTrue(len(re.findall(r'[^_ -]', self.bm.id)), 5)

    def test_created_at_type(self):
        self.assertEqual(type(self.bm.created_at), datetime)

    def test_updated_at_type(self):
        self.assertEqual(type(self.bm.updated_at), datetime)

    def test_str(self):
        res = f'[{self.bm.__class__.__name__}] ({self.bm.id}) '\
              f'{self.bm.__dict__}'
        self.assertEqual(str(self.bm), res)

    def test_save(self):
        self.bm.save()
        date = datetime.now()
        self.assertEqual(self.bm.updated_at.minute, date.minute)
        self.assertNotEqual(self.bm.created_at, self.bm.updated_at)

    def test_lenght_of_to_dict(self):
        self.assertEqual(len(self.bm.to_dict()), 4)

    def test_to_dict(self):
        self.assertEqual(self.bm.to_dict().get('__class__'), 'BaseModel')
        self.assertEqual(self.bm.to_dict().get('created_at'),
                         self.bm.created_at.isoformat())
        self.assertEqual(self.bm.to_dict().get('updated_at'),
                         self.bm.updated_at.isoformat())
        self.assertEqual(self.bm.to_dict().get('id'), self.bm.id)

    def test_create_obj_using_kwargs(self):
        bm1 = BaseModel(**self.bm.to_dict())
        self.assertEqual(bm1.to_dict(), self.bm.to_dict())
        self.assertEqual(bm1.id, self.bm.id)
        self.assertFalse(bm1 is self.bm)
        self.assertTrue(type(bm1.created_at), datetime)


if __name__ == '__main__':
    unittest.main()
