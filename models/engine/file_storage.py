#!/usr/bin/python3
"""
Contains File Storage
"""
import json
from models.base_model import BaseModel

classes = {'BaseModel': BaseModel}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    def __init__(self):
        """string - path to the JSON file"""
        self.__file_path = 'file.json'
        """dictionary - empty but will store all objects by <class name>.id"""
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        main_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({
            main_key: obj
        })

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for key in data:
                self.__objects[key] =
                classes[data[key]['__class__']](**data[key])
        except:
            pass
