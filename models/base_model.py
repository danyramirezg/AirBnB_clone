#!/usr/bin/python3
"""Module Base Model"""

import uuid
import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        """Constructor init"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime
        self.update_at = datetime

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        print("[{}] ({}) {}".format(classmethod, id, __dict__))

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime """

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        


