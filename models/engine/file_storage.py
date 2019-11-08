#!/usr/bin/python3
"""Module File Storage"""


class FileStorage:
    """"Class File Storage"""

    def __init__(self):
        """"Constructor method"""

        self.__file_path
        self.__objects

    def all(self):
        """"Public instance methods. Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing.
         If the file doesn’t exist, no exception should be raised)"""