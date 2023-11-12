#!/usr/bin/python3
"Defines the FileStorage class"
import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Stores all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        "returns the dictionary __objects"
        return self.__objects

    def new(self, obj):
        """adds a new object to __objects

        Args:
            obj (obj): The new object to add to __objects
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        "serializes __objects to the JSON file"
        data = dict(self.__objects)
        for k, v in data.items():
            data[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def reload(self):
        "deserializes the JSON file to __objects"
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {'BaseModel': BaseModel,
                   'User': User,
                   'State': State,
                   'City': City,
                   'Amenity': Amenity,
                   'Place': Place,
                   'Review': Review}

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for k, v in data.items():
                    self.__objects[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            pass
