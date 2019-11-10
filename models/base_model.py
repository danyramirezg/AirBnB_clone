#!/usr/bin/python3
"""Module Base Model"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor init"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs.keys():
                self.__dict__[key] = kwargs[key]
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
            return

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Return: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
