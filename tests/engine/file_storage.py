#!/usr/bin/python3
"""
This is the class file storage.
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User

class FileStorage(self):
    """
    Handles both serialization and deserialization of instance to/from
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__onjects[key] = obj

    def save(self):
        """
        Serializes the __objects to the JSON file (path: __file_path)
        """
        serialized_objs = {}
        for key, objs in FileStorage.__objects.items():
            serialized_objd[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objs, file)
    
    def reload(self):
        """
        Deserialize the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                serialized_objs = json.load(file)

            for key, value in serialized_objs.items():
                class_name, obj_id = key.split(".")
                clss = class_registry[class_name]
                obj = clss(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
