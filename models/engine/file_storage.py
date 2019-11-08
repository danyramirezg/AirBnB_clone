#!/usr/bin/python3
"""Module File Storage"""

import json
from base_model import BaseModel


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
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing.
         If the file doesn’t exist, no exception should be raised)"""

        with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
            dict_objects = json.load(f)
            for key, val in dict_objects.items():
                new_obj = BaseModel(**val)
                FileStorage.__objects[key] = new_obj
