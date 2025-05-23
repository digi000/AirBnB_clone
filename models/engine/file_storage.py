#!/usr/bin/env python3
"""serializes to file"""
import json, os
from ..base_model import BaseModel
from ..user import User
class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects"""
        return type(self).__objects

    def new(self, obj):
        type(self).__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        hj = {obj: type(self).__objects[obj].to_dict() for obj in type(self).__objects}
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(hj))

    def reload(self):
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, 'r') as f:
                text = f.read()
                if text:
                    objs = json.loads(text)
                    if objs:
                        for key, value in objs.items():
                            if key.split('.')[0] == BaseModel:
                                self.__objects[key] = BaseModel(**value)
                            else:
                                self.__objects[key] = User(**value)
