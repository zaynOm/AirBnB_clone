#!/usr/bin/python3
"Defines TestStorageModel class"
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import json
import os


class TestFileStorage(unittest.TestCase):
    "Unittests for FileStorage class"

    def setUp(self):
        self.file_path = storage._FileStorage__file_path
        self.objs = storage._FileStorage__objects
        self.bm = BaseModel()
        self.key = self.getKey(self.bm)

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    @staticmethod
    def getKey(obj):
        return obj.__class__.__name__ + '.' + obj.id

    def test_methods_exist(self):
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'reload'))

    def test_all(self):
        self.assertEqual(storage.all(), self.objs)

    def test_new(self):
        bm1 = BaseModel()
        storage.new(bm1)
        key = self.getKey(bm1)
        self.assertIn(key, self.objs)

    def test_save(self):
        storage.save()
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertIn(self.key, data)

    def test_reload(self):
        bm1 = BaseModel()
        storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        storage.reload()
        self.assertIn(self.getKey(bm1), self.objs)
        self.assertEqual(data[self.key], self.objs[self.key].to_dict())

    def test_path(self):
        "Test the existence of the JSON file"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
        storage.reload()


if __name__ == '__main__':
    unittest.main()
