#!/usr/bin/python3
"""Module File Storage"""

import json
from os.path import isfile
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review


class FileStorage:
    """"Class File Storage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self, file__path=None):
        """"Constructor method"""

        if file__path is not None:
            FileStorage.__file_path = file__path

    def all(self):
        """"Public instance methods. Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        JsObjs = {}
        for key, val in FileStorage.__objects.items():
            JsObjs[key] = val.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(JsObjs, f)

    def reload(self):
        """Deserialize the JSON file to __objects (only if __file_path exists.
         If the file doesn’t exist, no exception should be raised)"""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                dict_objects = json.load(f)
                for key, val in dict_objects.items():
                    new_obj = eval(val["__class__"])(**val)
                    FileStorage.__objects[key] = new_obj
