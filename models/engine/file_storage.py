#!/usr/bin/python3
""
import json


class FileStorage:
    ""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ""
        return self.__objects

    def new(self, obj):
        ""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        ""
        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def reload(self):
        ""
        from models.base_model import BaseModel
        from models.user import User

        classes = {'BaseModel': BaseModel, 'User': User}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for k, v in data.items():
                    self.__objects[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            pass