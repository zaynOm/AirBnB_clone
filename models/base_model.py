#!/usr/bin/python3
"This module defines the BaseClass"
from uuid import uuid4
from datetime import datetime, date
from models import storage


class BaseModel:
    """defines all common attributes/methods for other classes.

    Args:
        id (str): Unique instance id.
        created_at (datetime): Datetime when instance is created.
        updated_at (datetime): Datetime when instance is updated.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(v, fmt))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        "Returns the string representation of an instance"
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        "Updates `updated_at` with the current datetime."
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        "Returns the dictionary representation of the instance"
        data_dict = dict(self.__dict__)
        data_dict['__class__'] = self.__class__.__name__
        data_dict['created_at'] = self.created_at.isoformat()
        data_dict['updated_at'] = self.updated_at.isoformat()
        return data_dict
