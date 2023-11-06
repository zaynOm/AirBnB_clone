#!/usr/bin/python3
"This module defines the BaseClass"
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes.

    Args:
        id (str): Unique instance id.
        created_at (datetime): Datetime when instance is created.
        updated_at (datetime): Datetime when instance is updated.
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        "Returns the string representation of an instance"
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        "Updates `updated_at` with the current datetime."
        self.updated_at = datetime.now()

    def to_dict(self):
        "Returns the dictionary representation of the instance"
        data_dict = self.__dict__
        data_dict['__class__'] = self.__class__.__name__
        data_dict['created_at'] = str(self.created_at.isoformat('T'))
        data_dict['updated_at'] = str(self.updated_at.isoformat('T'))
        return data_dict
